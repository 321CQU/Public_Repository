from __future__ import annotations

import asyncio
import time
from typing import Awaitable, Callable, Optional

import grpc
from prometheus_client import CONTENT_TYPE_LATEST, Counter, Histogram, generate_latest

__all__ = [
    "GRPC_CLIENT_DURATION",
    "GRPC_CLIENT_REQUESTS",
    "GRPC_SERVER_DURATION",
    "GRPC_SERVER_REQUESTS",
    "GRPCMetricsClientInterceptor",
    "GRPCMetricsServerInterceptor",
    "instrument_grpc_callable",
    "start_metrics_server",
]


GRPC_CLIENT_DURATION = Histogram(
    "grpc_client_duration_seconds",
    "gRPC client request duration in seconds.",
    ("caller", "service", "method", "status_code"),
)

GRPC_CLIENT_REQUESTS = Counter(
    "grpc_client_requests_total",
    "Total gRPC client requests.",
    ("caller", "service", "method", "status_code"),
)

GRPC_SERVER_DURATION = Histogram(
    "grpc_server_duration_seconds",
    "gRPC server request duration in seconds.",
    ("service", "method", "status_code"),
)

GRPC_SERVER_REQUESTS = Counter(
    "grpc_server_requests_total",
    "Total gRPC server requests.",
    ("service", "method", "status_code"),
)


def _status_code(error: Exception | None) -> str:
    if error is None:
        return grpc.StatusCode.OK.name

    code = getattr(error, "code", None)
    if callable(code):
        try:
            value = code()
            return getattr(value, "name", str(value))
        except Exception:
            return grpc.StatusCode.UNKNOWN.name

    return grpc.StatusCode.UNKNOWN.name


def _split_rpc_method(path: str) -> tuple[str, str]:
    normalized = path.strip("/")
    if "/" not in normalized:
        return "unknown", normalized or "unknown"
    service, method = normalized.rsplit("/", 1)
    return service, method


def instrument_grpc_callable(
    func: Callable[..., Awaitable],
    *,
    caller: str,
    service: str,
    method: str,
) -> Callable[..., Awaitable]:
    async def wrapped(*args, **kwargs):
        start = time.perf_counter()
        error: Exception | None = None
        try:
            return await func(*args, **kwargs)
        except Exception as exc:
            error = exc
            raise
        finally:
            status_code = _status_code(error)
            duration = time.perf_counter() - start
            GRPC_CLIENT_DURATION.labels(caller, service, method, status_code).observe(duration)
            GRPC_CLIENT_REQUESTS.labels(caller, service, method, status_code).inc()

    return wrapped


class GRPCMetricsClientInterceptor(grpc.aio.UnaryUnaryClientInterceptor):
    def __init__(self, caller: str):
        self._caller = caller

    async def intercept_unary_unary(self, continuation, client_call_details, request):
        service, method = _split_rpc_method(client_call_details.method)
        start = time.perf_counter()
        error: Exception | None = None
        try:
            call = await continuation(client_call_details, request)
            return await call
        except Exception as exc:
            error = exc
            raise
        finally:
            status_code = _status_code(error)
            duration = time.perf_counter() - start
            GRPC_CLIENT_DURATION.labels(self._caller, service, method, status_code).observe(duration)
            GRPC_CLIENT_REQUESTS.labels(self._caller, service, method, status_code).inc()


class GRPCMetricsServerInterceptor(grpc.aio.ServerInterceptor):
    async def intercept_service(self, continuation, handler_call_details):
        handler = await continuation(handler_call_details)
        if handler is None or handler.unary_unary is None:
            return handler

        service, method = _split_rpc_method(handler_call_details.method)

        async def unary_unary(request, context):
            start = time.perf_counter()
            error: Exception | None = None
            try:
                return await handler.unary_unary(request, context)
            except Exception as exc:
                error = exc
                raise
            finally:
                status_code = _status_code(error)
                duration = time.perf_counter() - start
                GRPC_SERVER_DURATION.labels(service, method, status_code).observe(duration)
                GRPC_SERVER_REQUESTS.labels(service, method, status_code).inc()

        return grpc.unary_unary_rpc_method_handler(
            unary_unary,
            request_deserializer=handler.request_deserializer,
            response_serializer=handler.response_serializer,
        )


async def _handle_metrics_request(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    try:
        request_line = await reader.readline()
        request_parts = request_line.decode("ascii", errors="ignore").split()
        path = request_parts[1] if len(request_parts) >= 2 else ""
        while await reader.readline() not in {b"\r\n", b"\n", b""}:
            pass

        if path != "/metrics":
            body = b"Not Found"
            status = b"404 Not Found"
            content_type = b"text/plain; charset=utf-8"
        else:
            body = generate_latest()
            status = b"200 OK"
            content_type = CONTENT_TYPE_LATEST.encode("ascii")

        writer.write(
            b"HTTP/1.1 "
            + status
            + b"\r\nContent-Type: "
            + content_type
            + b"\r\nContent-Length: "
            + str(len(body)).encode("ascii")
            + b"\r\nConnection: close\r\n\r\n"
            + body
        )
        await writer.drain()
    finally:
        writer.close()
        await writer.wait_closed()


async def start_metrics_server(port: int | str | None, host: str = "0.0.0.0") -> Optional[asyncio.AbstractServer]:
    if port is None:
        return None

    try:
        port_value = int(port)
    except (TypeError, ValueError) as exc:
        raise RuntimeError(f"Invalid metrics port: {port!r}") from exc

    if port_value <= 0:
        return None

    return await asyncio.start_server(_handle_metrics_request, host=host, port=port_value)

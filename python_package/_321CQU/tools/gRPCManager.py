from __future__ import annotations

from contextlib import asynccontextmanager
import os
from typing import Any, Tuple

from grpc.aio import Channel, insecure_channel

from .ConfigHandler import _CONFIG_HANDLER, ConfigHandler
from .gRPCMetrics import instrument_grpc_callable
from .Singleton import Singleton

__all__ = ['gRPCManager', 'MockGRPCManager']

from ..service import ServiceEnum


class _InstrumentedStub:
    def __init__(self, stub: Any, caller: str, service: ServiceEnum):
        self._stub = stub
        self._caller = caller
        self._service = service

    def __getattr__(self, item: str):
        target = getattr(self._stub, item)
        if not callable(target):
            return target
        return instrument_grpc_callable(
            target,
            caller=self._caller,
            service=self._service.value,
            method=item,
        )


class gRPCManager(metaclass=Singleton):
    def __init__(self, handler: ConfigHandler = _CONFIG_HANDLER, caller: str | None = None):
        all_options = handler.get_options('ServiceSetting')

        service_hosts = list(filter(lambda x: x.endswith('_service_host'), all_options))
        service_ports = list(filter(lambda x: x.endswith('_service_port'), all_options))
        self._service_host = {}
        self._service_ports = {}

        for host in service_hosts:
            self._service_host.update({
                host: handler.get_config("ServiceSetting", host)
            })

        for port in service_ports:
            self._service_ports.update({
                port: handler.get_config("ServiceSetting", port)
            })
        self._channels: dict[str, Channel] = {}
        self._caller = caller or os.getenv("SERVICE_NAME", "unknown")

    def get_service_config(self, service: ServiceEnum) -> Tuple[str, str]:
        return (self._service_host[service.service_name + "_service_host"],
                self._service_ports[service.service_name + "_service_port"])

    def _get_channel(self, service: ServiceEnum) -> Channel:
        host = self._service_host[service.service_name + "_service_host"]
        port = self._service_ports[service.service_name + "_service_port"]
        target_url = host + ":" + port

        channel = self._channels.get(target_url)
        if channel is not None:
            return channel

        channel = insecure_channel(target_url)
        self._channels[target_url] = channel
        return channel

    async def close_all(self) -> None:
        for channel in self._channels.values():
            await channel.close()
        self._channels.clear()

    @asynccontextmanager
    async def get_stub(self, service: ServiceEnum):
        if service.is_http_service:
            raise RuntimeError("该服务不是gRPC服务")

        target = service._get_stub_class()

        if target is not None:
            yield _InstrumentedStub(target(self._get_channel(service)), self._caller, service)


class MockGRPCManager(gRPCManager):
    @asynccontextmanager
    async def get_stub(self, service: ServiceEnum):
        yield service._get_mock_stub_class()()

#!/usr/bin/env python3
import argparse
import asyncio
import json
import statistics
import time
from urllib import request as urllib_request

import grpc
from micro_services_protobuf.edu_admin_center import eac_models_pb2, eac_service_pb2_grpc
from micro_services_protobuf.mycqu_service import mycqu_request_response_pb2, mycqu_service_pb2_grpc


def _percentile(values, percent):
    if not values:
        return 0.0
    ordered = sorted(values)
    index = min(len(ordered) - 1, round((percent / 100) * (len(ordered) - 1)))
    return ordered[index]


def _summary(values):
    if not values:
        return {
            "count": 0,
            "avg_ms": 0.0,
            "p50_ms": 0.0,
            "p95_ms": 0.0,
            "p99_ms": 0.0,
        }

    return {
        "count": len(values),
        "avg_ms": round(statistics.fmean(values) * 1000, 3),
        "p50_ms": round(_percentile(values, 50) * 1000, 3),
        "p95_ms": round(_percentile(values, 95) * 1000, 3),
        "p99_ms": round(_percentile(values, 99) * 1000, 3),
    }


async def _time_async(label, count, func):
    values = []
    for _ in range(count):
        start = time.perf_counter()
        await func()
        values.append(time.perf_counter() - start)
    return label, values


async def _benchmark_direct_mycqu(args):
    channel = grpc.aio.insecure_channel(args.mycqu_target)
    stub = mycqu_service_pb2_grpc.MycquFetcherStub(channel)
    login = mycqu_request_response_pb2.BaseLoginInfo(auth=args.auth, password=args.password)
    req = mycqu_request_response_pb2.FetchScoreRequest(base_login_info=login, is_minor=False)
    try:
        return await _time_async("direct_mycqu_fetch_score", args.iterations, lambda: stub.FetchScore(req))
    finally:
        await channel.close()


async def _benchmark_eac(args):
    channel = grpc.aio.insecure_channel(args.eac_target)
    stub = eac_service_pb2_grpc.EduAdminCenterStub(channel)
    login = mycqu_request_response_pb2.BaseLoginInfo(auth=args.auth, password=args.password)
    req = eac_models_pb2.FetchScoreRequest(base_login_info=login, sid=args.sid, is_minor=False)
    try:
        return await _time_async("eac_fetch_score", args.iterations, lambda: stub.FetchScore(req))
    finally:
        await channel.close()


async def _benchmark_gateway(args):
    if not args.gateway_score_url:
        return None

    payload = json.dumps({"sid": args.sid, "is_minor": False}).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    if args.gateway_token:
        headers["Authorization"] = f"Bearer {args.gateway_token}"

    async def call():
        req = urllib_request.Request(args.gateway_score_url, data=payload, headers=headers, method="POST")
        def open_and_read():
            with urllib_request.urlopen(req, timeout=args.http_timeout) as response:
                response.read()

        await asyncio.to_thread(open_and_read)

    return await _time_async("gateway_fetch_score", args.iterations, call)


async def main():
    parser = argparse.ArgumentParser(description="Benchmark 321CQU microservice hop overhead.")
    parser.add_argument("--mycqu-target", default="localhost:53211")
    parser.add_argument("--eac-target", default="localhost:53212")
    parser.add_argument("--gateway-score-url")
    parser.add_argument("--gateway-token")
    parser.add_argument("--auth", required=True)
    parser.add_argument("--password", required=True)
    parser.add_argument("--sid", required=True)
    parser.add_argument("--iterations", type=int, default=20)
    parser.add_argument("--http-timeout", type=int, default=30)
    args = parser.parse_args()

    results = [
        await _benchmark_direct_mycqu(args),
        await _benchmark_eac(args),
        await _benchmark_gateway(args),
    ]
    summaries = {label: _summary(values) for item in results if item is not None for label, values in [item]}
    print(json.dumps(summaries, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    asyncio.run(main())

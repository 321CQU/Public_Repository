# 321CQU 后端公共仓库

目前包括：
- 后端gRPC所需全部protobuf文件
- 部分被多个微服务所依赖的tool（例如，抽象数据库管理类、配置文件读取类、单例模式metaclass）

## 微服务性能基准

`tools/benchmark_microservice_overhead.py` 可用于对比 direct mycqu gRPC、EduAdminCenter 聚合调用和可选 API Gateway HTTP 调用的耗时分布：

```bash
PYTHONPATH=./python_package python tools/benchmark_microservice_overhead.py \
  --auth <统一认证号> \
  --password <密码> \
  --sid <学号> \
  --iterations 20
```

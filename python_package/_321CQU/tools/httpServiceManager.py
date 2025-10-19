from .ConfigHandler import ConfigHandler, _CONFIG_HANDLER
from .Singleton import Singleton

from ..service import ServiceEnum
from ..service_handler import ServiceHandler


class HttpServiceManager(metaclass=Singleton):
    def __init__(self, handler: ConfigHandler = _CONFIG_HANDLER):
        # 初始化时创建每个ServiceHandler子类的实例
        self.service_instances = [cls() for cls in ServiceHandler.__subclasses__()]
        all_options = handler.get_options('ServiceSetting')

        service_hosts = list(filter(lambda x: x.endswith('_http_host'), all_options))
        service_ports = list(filter(lambda x: x.endswith('_http_port'), all_options))
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

    def host(self, service: ServiceEnum) -> str:
        if not service.is_http_service:
            raise RuntimeError("该服务不是http服务")
        for instance in self.service_instances:
            if instance.support(name=service):
                host = self._service_host[instance.get_service_name + "_http_host"]
                port = self._service_ports[instance.get_service_name + "_http_port"]
                return host + ":" + port

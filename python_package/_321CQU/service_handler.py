from python_package._321CQU.service import ServiceEnum
from abc import ABC, abstractmethod
from micro_services_protobuf.notification_center import service_pb2_grpc as notification_grpc
from micro_services_protobuf.mycqu_service import mycqu_service_pb2_grpc as mycqu_grpc
from micro_services_protobuf.edu_admin_center import eac_service_pb2_grpc as eac_grpc
from micro_services_protobuf.course_score_query import service_pb2_grpc as csq_grpc
from micro_services_protobuf.control_center import control_center_service_pb2_grpc as cc_grpc


class ServiceHandler(ABC):
    """
    服务处理器抽象类
    """

    @abstractmethod
    def support(self, name: ServiceEnum) -> bool:
        """
        判断是否支持该服务
        @param name: 服务名枚举
        """
        pass

    @abstractmethod
    @property
    def get_service_name(self) -> str:
        """
        获取服务名
        """
        pass

    @abstractmethod
    def get_stub_class(self):
        """
        获取stub类
        """
        pass


class WechatManagerHandler(ServiceHandler):
    """
    微信管理器服务处理器
    """

    def support(self, name: ServiceEnum) -> bool:
        return name == ServiceEnum.WechatManager

    def get_service_name(self) -> str:
        return 'wechat_manager'

    def get_stub_class(self):
        pass


class ApnsServiceHandler(ServiceHandler):
    """
    Apns服务处理器
    """

    def support(self, name: ServiceEnum) -> bool:
        return name == ServiceEnum.ApnsService

    def get_service_name(self) -> str:
        return 'notification_center'

    def get_stub_class(self):
        return notification_grpc.ApnsStub


class WechatServiceHandler(ServiceHandler):
    """
    微信服务处理器
    """

    def support(self, name: ServiceEnum) -> bool:
        return name == ServiceEnum.WechatService

    def get_service_name(self) -> str:
        return 'notification_center'

    def get_stub_class(self):
        return notification_grpc.WechatStub


class NotificationServiceHandler(ServiceHandler):
    """
    通知服务处理器
    """

    def support(self, name: ServiceEnum) -> bool:
        return name == ServiceEnum.NotificationService

    def get_service_name(self) -> str:
        return 'notification_center'

    def get_stub_class(self):
        return notification_grpc.NotificationStub


class ImportantInfoServiceHandler(ServiceHandler):
    """
    重要信息服务处理器
    """

    def support(self, name: ServiceEnum) -> bool:
        return name == ServiceEnum.ImportantInfoService

    def get_service_name(self) -> str:
        return 'important_info'

    def get_stub_class(self):
        return cc_grpc.ImportantInfoServiceStub


class MycquServiceHandler(ServiceHandler):
    """
    Mycqu服务处理器
    """

    def support(self, name: ServiceEnum) -> bool:
        return name == ServiceEnum.MycquService

    def get_service_name(self) -> str:
        return 'mycqu'

    def get_stub_class(self):
        return mycqu_grpc.MycquFetcherStub


class CardServiceHandler(ServiceHandler):
    """
    一卡通服务处理器
    """

    def support(self, name: ServiceEnum) -> bool:
        return name == ServiceEnum.CardService

    def get_service_name(self) -> str:
        return 'mycqu'

    def get_stub_class(self):
        return mycqu_grpc.CardFetcherStub


class LibraryServiceHandler(ServiceHandler):
    """
    图书馆服务处理器
    """

    def support(self, name: ServiceEnum) -> bool:
        return name == ServiceEnum.LibraryService

    def get_service_name(self) -> str:
        return 'mycqu'

    def get_stub_class(self):
        return mycqu_grpc.LibraryFetcherStub


class EduAdminCenterHandler(ServiceHandler):
    """
    教务中心服务处理器
    """

    def support(self, name: ServiceEnum) -> bool:
        return name == ServiceEnum.EduAdminCenter

    def get_service_name(self) -> str:
        return 'edu_admin_center'

    def get_stub_class(self):
        return eac_grpc.EduAdminCenterStub


class CourseScoreQueryHandler(ServiceHandler):
    """
    课程成绩查询服务处理器
    """

    def support(self, name: ServiceEnum) -> bool:
        return name == ServiceEnum.CourseScoreQuery

    def get_service_name(self) -> str:
        return 'course_score_query'

    def get_stub_class(self):
        return csq_grpc.CourseScoreQueryStub

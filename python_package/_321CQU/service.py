from enum import Enum

from ._mock import MockApnStub
from micro_services_protobuf.notification_center import service_pb2_grpc as notification_grpc
from micro_services_protobuf.mycqu_service import mycqu_service_pb2_grpc as mycqu_grpc
from micro_services_protobuf.edu_admin_center import eac_service_pb2_grpc as eac_grpc
from micro_services_protobuf.course_score_query import service_pb2_grpc as csq_grpc
from micro_services_protobuf.control_center import control_center_service_pb2_grpc as cc_grpc


class ServiceEnum(str, Enum):
    WechatManager = 'wechat_manager'

    ApnsService = 'apns_service'
    WechatService = 'wechat_service'
    NotificationService = 'notification_service'
    ImportantInfoService = 'important_info_service'

    MycquService = 'mycqu_service'
    CardService = 'card_service'
    LibraryService = 'library_service'

    EduAdminCenter = 'edu_admin_center'

    CourseScoreQuery = 'course_score_query'

    @property
    def service_name(self) -> str:
        if self == ServiceEnum.WechatManager:
            return 'wechat_manager'
        elif self == ServiceEnum.ApnsService:
            return 'notification_center'
        elif self == ServiceEnum.WechatService:
            return 'notification_center'
        elif self == ServiceEnum.NotificationService:
            return 'notification_center'
        elif self == ServiceEnum.ImportantInfoService:
            return 'important_info'
        elif self == ServiceEnum.MycquService:
            return 'mycqu'
        elif self == ServiceEnum.CardService:
            return 'mycqu'
        elif self == ServiceEnum.LibraryService:
            return 'mycqu'
        elif self == ServiceEnum.EduAdminCenter:
            return 'edu_admin_center'
        elif self == ServiceEnum.CourseScoreQuery:
            return 'course_score_query'

    @property
    def is_http_service(self):
        if self == ServiceEnum.WechatManager:
            return True

        return False

    def _get_stub_class(self):
        if self == ServiceEnum.ApnsService:
            return notification_grpc.ApnsStub
        elif self == ServiceEnum.WechatService:
            return notification_grpc.WechatStub
        elif self == ServiceEnum.NotificationService:
            return notification_grpc.NotificationStub
        elif self == ServiceEnum.ImportantInfoService:
            return cc_grpc.ImportantInfoServiceStub
        elif self == ServiceEnum.MycquService:
            return mycqu_grpc.MycquFetcherStub
        elif self == ServiceEnum.CardService:
            return mycqu_grpc.CardFetcherStub
        elif self == ServiceEnum.LibraryService:
            return mycqu_grpc.LibraryFetcherStub
        elif self == ServiceEnum.EduAdminCenter:
            return eac_grpc.EduAdminCenterStub
        elif self == ServiceEnum.CourseScoreQuery:
            return csq_grpc.CourseScoreQueryStub
        else:
            raise RuntimeError("未提供对应服务Stub")

    def _get_mock_stub_class(self):
        if self == ServiceEnum.ApnsService:
            return MockApnStub
        else:
            raise RuntimeError("未提供对应Mock")

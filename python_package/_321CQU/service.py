from enum import Enum

from ._mock import MockApnStub
from micro_services_protobuf.notification_center import service_pb2_grpc as notification_grpc
from micro_services_protobuf.mycqu_service import mycqu_service_pb2_grpc as mycqu_grpc
from micro_services_protobuf.edu_admin_center import eac_service_pb2_grpc as eac_grpc


class ServiceEnum(str, Enum):
    WechatManager = 'wechat_manager'

    ApnsService = 'apns_service'
    WechatService = 'wechat_service'
    NotificationService = 'notification_service'

    MycquService = 'mycqu_service'
    CardService = 'card_service'

    EduAdminCenter = 'edu_admin_center'

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
        elif self == ServiceEnum.MycquService:
            return 'mycqu_service'
        elif self == ServiceEnum.CardService:
            return 'mycqu_service'
        elif self == ServiceEnum.EduAdminCenter:
            return 'edu_admin_center'

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
        elif self == ServiceEnum.MycquService:
            return mycqu_grpc.MycquFetcherStub
        elif self == ServiceEnum.CardService:
            return mycqu_grpc.CardFetcherStub
        elif self == ServiceEnum.EduAdminCenter:
            return eac_grpc.EduAdminCenterStub
        else:
            raise RuntimeError("未提供对应服务Stub")

    def _get_mock_stub_class(self):
        if self == ServiceEnum.ApnsService:
            return MockApnStub
        else:
            raise RuntimeError("未提供对应Mock")
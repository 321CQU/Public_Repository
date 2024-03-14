from enum import Enum

from ._mock import MockApnStub


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
    def is_http_service(self):
        if self == ServiceEnum.WechatManager:
            return True

        return False

    def _get_mock_stub_class(self):
        if self == ServiceEnum.ApnsService:
            return MockApnStub
        else:
            raise RuntimeError("未提供对应Mock")

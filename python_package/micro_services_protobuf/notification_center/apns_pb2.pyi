from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SendApnsNotificationRequest(_message.Message):
    __slots__ = ["apn", "notification"]
    class AppleNotification(_message.Message):
        __slots__ = ["alert", "badge", "category"]
        class AppleAlert(_message.Message):
            __slots__ = ["body", "subtitle", "title"]
            BODY_FIELD_NUMBER: _ClassVar[int]
            SUBTITLE_FIELD_NUMBER: _ClassVar[int]
            TITLE_FIELD_NUMBER: _ClassVar[int]
            body: str
            subtitle: str
            title: str
            def __init__(self, title: _Optional[str] = ..., subtitle: _Optional[str] = ..., body: _Optional[str] = ...) -> None: ...
        ALERT_FIELD_NUMBER: _ClassVar[int]
        BADGE_FIELD_NUMBER: _ClassVar[int]
        CATEGORY_FIELD_NUMBER: _ClassVar[int]
        alert: SendApnsNotificationRequest.AppleNotification.AppleAlert
        badge: int
        category: str
        def __init__(self, alert: _Optional[_Union[SendApnsNotificationRequest.AppleNotification.AppleAlert, _Mapping]] = ..., badge: _Optional[int] = ..., category: _Optional[str] = ...) -> None: ...
    APN_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    apn: bytes
    notification: SendApnsNotificationRequest.AppleNotification
    def __init__(self, apn: _Optional[bytes] = ..., notification: _Optional[_Union[SendApnsNotificationRequest.AppleNotification, _Mapping]] = ...) -> None: ...

class SetUserApnsRequest(_message.Message):
    __slots__ = ["apn", "uid"]
    APN_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    apn: bytes
    uid: bytes
    def __init__(self, uid: _Optional[bytes] = ..., apn: _Optional[bytes] = ...) -> None: ...

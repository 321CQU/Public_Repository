from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NOTIFICATION_EVENT(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    NOTIFICATION_EVENT_SCORE: _ClassVar[NOTIFICATION_EVENT]
NOTIFICATION_EVENT_SCORE: NOTIFICATION_EVENT

class UpdateEventSubscribeRequest(_message.Message):
    __slots__ = ["uid", "event", "is_subscribe", "extra_data"]
    class ExtraData(_message.Message):
        __slots__ = ["auth", "password", "extra_data"]
        AUTH_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_FIELD_NUMBER: _ClassVar[int]
        EXTRA_DATA_FIELD_NUMBER: _ClassVar[int]
        auth: str
        password: str
        extra_data: str
        def __init__(self, auth: _Optional[str] = ..., password: _Optional[str] = ..., extra_data: _Optional[str] = ...) -> None: ...
    UID_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    IS_SUBSCRIBE_FIELD_NUMBER: _ClassVar[int]
    EXTRA_DATA_FIELD_NUMBER: _ClassVar[int]
    uid: bytes
    event: NOTIFICATION_EVENT
    is_subscribe: bool
    extra_data: UpdateEventSubscribeRequest.ExtraData
    def __init__(self, uid: _Optional[bytes] = ..., event: _Optional[_Union[NOTIFICATION_EVENT, str]] = ..., is_subscribe: bool = ..., extra_data: _Optional[_Union[UpdateEventSubscribeRequest.ExtraData, _Mapping]] = ...) -> None: ...

class FetchSubscribeInfoResponse(_message.Message):
    __slots__ = ["events"]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedScalarFieldContainer[NOTIFICATION_EVENT]
    def __init__(self, events: _Optional[_Iterable[_Union[NOTIFICATION_EVENT, str]]] = ...) -> None: ...

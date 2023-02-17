from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
NOTIFICATION_EVENT_SCORE: NOTIFICATION_EVENT

class FetchSubscribeInfoResponse(_message.Message):
    __slots__ = ["events"]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedScalarFieldContainer[NOTIFICATION_EVENT]
    def __init__(self, events: _Optional[_Iterable[_Union[NOTIFICATION_EVENT, str]]] = ...) -> None: ...

class UpdateEventSubscribeRequest(_message.Message):
    __slots__ = ["event", "is_subscribe", "uid"]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    IS_SUBSCRIBE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    event: NOTIFICATION_EVENT
    is_subscribe: bool
    uid: bytes
    def __init__(self, uid: _Optional[bytes] = ..., event: _Optional[_Union[NOTIFICATION_EVENT, str]] = ..., is_subscribe: bool = ...) -> None: ...

class NOTIFICATION_EVENT(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

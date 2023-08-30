from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DefaultResponse(_message.Message):
    __slots__ = ["msg"]
    MSG_FIELD_NUMBER: _ClassVar[int]
    msg: str
    def __init__(self, msg: _Optional[str] = ...) -> None: ...

class UserId(_message.Message):
    __slots__ = ["uid"]
    UID_FIELD_NUMBER: _ClassVar[int]
    uid: bytes
    def __init__(self, uid: _Optional[bytes] = ...) -> None: ...

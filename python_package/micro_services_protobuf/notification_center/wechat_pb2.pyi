from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HandleWechatServerEventRequest(_message.Message):
    __slots__ = ["is_accept", "openid", "template_id"]
    IS_ACCEPT_FIELD_NUMBER: _ClassVar[int]
    OPENID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    is_accept: bool
    openid: str
    template_id: str
    def __init__(self, openid: _Optional[str] = ..., template_id: _Optional[str] = ..., is_accept: bool = ...) -> None: ...

class SetUserOpenIdRequest(_message.Message):
    __slots__ = ["code", "uid"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    code: str
    uid: bytes
    def __init__(self, uid: _Optional[bytes] = ..., code: _Optional[str] = ...) -> None: ...

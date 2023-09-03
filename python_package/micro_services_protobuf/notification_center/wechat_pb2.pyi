from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetUserOpenIdRequest(_message.Message):
    __slots__ = ["uid", "code"]
    UID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    uid: bytes
    code: str
    def __init__(self, uid: _Optional[bytes] = ..., code: _Optional[str] = ...) -> None: ...

class HandleWechatServerEventRequest(_message.Message):
    __slots__ = ["openid", "template_id", "is_accept"]
    OPENID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    IS_ACCEPT_FIELD_NUMBER: _ClassVar[int]
    openid: str
    template_id: str
    is_accept: bool
    def __init__(self, openid: _Optional[str] = ..., template_id: _Optional[str] = ..., is_accept: bool = ...) -> None: ...

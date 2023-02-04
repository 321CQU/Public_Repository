from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DefaultResponse(_message.Message):
    __slots__ = ["data", "msg", "status"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    data: _any_pb2.Any
    msg: str
    status: int
    def __init__(self, status: _Optional[int] = ..., msg: _Optional[str] = ..., data: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

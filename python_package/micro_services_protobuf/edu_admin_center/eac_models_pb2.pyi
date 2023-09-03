from micro_services_protobuf.mycqu_service import mycqu_model_pb2 as _mycqu_model_pb2
from micro_services_protobuf.mycqu_service import mycqu_request_response_pb2 as _mycqu_request_response_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ValidateAuthResponse(_message.Message):
    __slots__ = ["sid", "auth", "name", "uid"]
    SID_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    sid: str
    auth: str
    name: str
    uid: bytes
    def __init__(self, sid: _Optional[str] = ..., auth: _Optional[str] = ..., name: _Optional[str] = ..., uid: _Optional[bytes] = ...) -> None: ...

class FetchCourseTimetableRequest(_message.Message):
    __slots__ = ["login_info", "code", "offset"]
    LOGIN_INFO_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    login_info: _mycqu_request_response_pb2.BaseLoginInfo
    code: str
    offset: int
    def __init__(self, login_info: _Optional[_Union[_mycqu_request_response_pb2.BaseLoginInfo, _Mapping]] = ..., code: _Optional[str] = ..., offset: _Optional[int] = ...) -> None: ...

class FetchCourseTimetableResponse(_message.Message):
    __slots__ = ["course_timetables", "start_date", "end_date", "session_name"]
    COURSE_TIMETABLES_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    SESSION_NAME_FIELD_NUMBER: _ClassVar[int]
    course_timetables: _containers.RepeatedCompositeFieldContainer[_mycqu_model_pb2.CourseTimetable]
    start_date: str
    end_date: str
    session_name: str
    def __init__(self, course_timetables: _Optional[_Iterable[_Union[_mycqu_model_pb2.CourseTimetable, _Mapping]]] = ..., start_date: _Optional[str] = ..., end_date: _Optional[str] = ..., session_name: _Optional[str] = ...) -> None: ...

class FetchScoreRequest(_message.Message):
    __slots__ = ["base_login_info", "sid", "is_minor"]
    BASE_LOGIN_INFO_FIELD_NUMBER: _ClassVar[int]
    SID_FIELD_NUMBER: _ClassVar[int]
    IS_MINOR_FIELD_NUMBER: _ClassVar[int]
    base_login_info: _mycqu_request_response_pb2.BaseLoginInfo
    sid: str
    is_minor: bool
    def __init__(self, base_login_info: _Optional[_Union[_mycqu_request_response_pb2.BaseLoginInfo, _Mapping]] = ..., sid: _Optional[str] = ..., is_minor: bool = ...) -> None: ...

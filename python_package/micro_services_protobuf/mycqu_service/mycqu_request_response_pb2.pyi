from micro_services_protobuf.mycqu_service import mycqu_model_pb2 as _mycqu_model_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BaseLoginInfo(_message.Message):
    __slots__ = ["auth", "password"]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    auth: str
    password: str
    def __init__(self, auth: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class FetchAllSessionInfoResponse(_message.Message):
    __slots__ = ["session_infos"]
    SESSION_INFOS_FIELD_NUMBER: _ClassVar[int]
    session_infos: _containers.RepeatedCompositeFieldContainer[_mycqu_model_pb2.CquSessionInfo]
    def __init__(self, session_infos: _Optional[_Iterable[_Union[_mycqu_model_pb2.CquSessionInfo, _Mapping]]] = ...) -> None: ...

class FetchAllSessionResponse(_message.Message):
    __slots__ = ["sessions"]
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    sessions: _containers.RepeatedCompositeFieldContainer[_mycqu_model_pb2.CquSession]
    def __init__(self, sessions: _Optional[_Iterable[_Union[_mycqu_model_pb2.CquSession, _Mapping]]] = ...) -> None: ...

class FetchBillResponse(_message.Message):
    __slots__ = ["bills"]
    BILLS_FIELD_NUMBER: _ClassVar[int]
    bills: _containers.RepeatedCompositeFieldContainer[_mycqu_model_pb2.Bill]
    def __init__(self, bills: _Optional[_Iterable[_Union[_mycqu_model_pb2.Bill, _Mapping]]] = ...) -> None: ...

class FetchCourseTimetableRequest(_message.Message):
    __slots__ = ["base_login_info", "code", "session"]
    BASE_LOGIN_INFO_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    base_login_info: BaseLoginInfo
    code: str
    session: _mycqu_model_pb2.CquSession
    def __init__(self, base_login_info: _Optional[_Union[BaseLoginInfo, _Mapping]] = ..., code: _Optional[str] = ..., session: _Optional[_Union[_mycqu_model_pb2.CquSession, _Mapping]] = ...) -> None: ...

class FetchCourseTimetableResponse(_message.Message):
    __slots__ = ["course_timetables"]
    COURSE_TIMETABLES_FIELD_NUMBER: _ClassVar[int]
    course_timetables: _containers.RepeatedCompositeFieldContainer[_mycqu_model_pb2.CourseTimetable]
    def __init__(self, course_timetables: _Optional[_Iterable[_Union[_mycqu_model_pb2.CourseTimetable, _Mapping]]] = ...) -> None: ...

class FetchEnergyFeeRequest(_message.Message):
    __slots__ = ["base_login_info", "is_hu_xi", "room"]
    BASE_LOGIN_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_HU_XI_FIELD_NUMBER: _ClassVar[int]
    ROOM_FIELD_NUMBER: _ClassVar[int]
    base_login_info: BaseLoginInfo
    is_hu_xi: bool
    room: str
    def __init__(self, base_login_info: _Optional[_Union[BaseLoginInfo, _Mapping]] = ..., is_hu_xi: bool = ..., room: _Optional[str] = ...) -> None: ...

class FetchEnrollCourseInfoRequest(_message.Message):
    __slots__ = ["base_login_info", "is_major"]
    BASE_LOGIN_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_MAJOR_FIELD_NUMBER: _ClassVar[int]
    base_login_info: BaseLoginInfo
    is_major: bool
    def __init__(self, base_login_info: _Optional[_Union[BaseLoginInfo, _Mapping]] = ..., is_major: bool = ...) -> None: ...

class FetchEnrollCourseInfoResponse(_message.Message):
    __slots__ = ["result"]
    class EnrollCourseInfos(_message.Message):
        __slots__ = ["info"]
        INFO_FIELD_NUMBER: _ClassVar[int]
        info: _containers.RepeatedCompositeFieldContainer[_mycqu_model_pb2.EnrollCourseInfo]
        def __init__(self, info: _Optional[_Iterable[_Union[_mycqu_model_pb2.EnrollCourseInfo, _Mapping]]] = ...) -> None: ...
    class ResultEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: FetchEnrollCourseInfoResponse.EnrollCourseInfos
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[FetchEnrollCourseInfoResponse.EnrollCourseInfos, _Mapping]] = ...) -> None: ...
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.MessageMap[str, FetchEnrollCourseInfoResponse.EnrollCourseInfos]
    def __init__(self, result: _Optional[_Mapping[str, FetchEnrollCourseInfoResponse.EnrollCourseInfos]] = ...) -> None: ...

class FetchEnrollCourseItemRequest(_message.Message):
    __slots__ = ["base_login_info", "id", "is_major"]
    BASE_LOGIN_INFO_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_MAJOR_FIELD_NUMBER: _ClassVar[int]
    base_login_info: BaseLoginInfo
    id: str
    is_major: bool
    def __init__(self, base_login_info: _Optional[_Union[BaseLoginInfo, _Mapping]] = ..., id: _Optional[str] = ..., is_major: bool = ...) -> None: ...

class FetchEnrollCourseItemResponse(_message.Message):
    __slots__ = ["enroll_course_items"]
    ENROLL_COURSE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    enroll_course_items: _containers.RepeatedCompositeFieldContainer[_mycqu_model_pb2.EnrollCourseItem]
    def __init__(self, enroll_course_items: _Optional[_Iterable[_Union[_mycqu_model_pb2.EnrollCourseItem, _Mapping]]] = ...) -> None: ...

class FetchExamRequest(_message.Message):
    __slots__ = ["base_login_info", "stu_id"]
    BASE_LOGIN_INFO_FIELD_NUMBER: _ClassVar[int]
    STU_ID_FIELD_NUMBER: _ClassVar[int]
    base_login_info: BaseLoginInfo
    stu_id: str
    def __init__(self, base_login_info: _Optional[_Union[BaseLoginInfo, _Mapping]] = ..., stu_id: _Optional[str] = ...) -> None: ...

class FetchExamResponse(_message.Message):
    __slots__ = ["exams"]
    EXAMS_FIELD_NUMBER: _ClassVar[int]
    exams: _containers.RepeatedCompositeFieldContainer[_mycqu_model_pb2.Exam]
    def __init__(self, exams: _Optional[_Iterable[_Union[_mycqu_model_pb2.Exam, _Mapping]]] = ...) -> None: ...

class FetchScoreRequest(_message.Message):
    __slots__ = ["base_login_info", "is_minor"]
    BASE_LOGIN_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_MINOR_FIELD_NUMBER: _ClassVar[int]
    base_login_info: BaseLoginInfo
    is_minor: bool
    def __init__(self, base_login_info: _Optional[_Union[BaseLoginInfo, _Mapping]] = ..., is_minor: bool = ...) -> None: ...

class FetchScoreResponse(_message.Message):
    __slots__ = ["scores"]
    SCORES_FIELD_NUMBER: _ClassVar[int]
    scores: _containers.RepeatedCompositeFieldContainer[_mycqu_model_pb2.Score]
    def __init__(self, scores: _Optional[_Iterable[_Union[_mycqu_model_pb2.Score, _Mapping]]] = ...) -> None: ...

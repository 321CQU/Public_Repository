from micro_services_protobuf.mycqu_service import mycqu_model_pb2 as _mycqu_model_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FindCourseByNameRequest(_message.Message):
    __slots__ = ["course_name", "teacher_name"]
    COURSE_NAME_FIELD_NUMBER: _ClassVar[int]
    TEACHER_NAME_FIELD_NUMBER: _ClassVar[int]
    course_name: str
    teacher_name: str
    def __init__(self, course_name: _Optional[str] = ..., teacher_name: _Optional[str] = ...) -> None: ...

class FindCourseByNameResponse(_message.Message):
    __slots__ = ["courses"]
    COURSES_FIELD_NUMBER: _ClassVar[int]
    courses: _containers.RepeatedCompositeFieldContainer[_mycqu_model_pb2.Course]
    def __init__(self, courses: _Optional[_Iterable[_Union[_mycqu_model_pb2.Course, _Mapping]]] = ...) -> None: ...

class FetchLayeredScoreDetailRequest(_message.Message):
    __slots__ = ["course_code"]
    COURSE_CODE_FIELD_NUMBER: _ClassVar[int]
    course_code: str
    def __init__(self, course_code: _Optional[str] = ...) -> None: ...

class LayeredScoreDetail(_message.Message):
    __slots__ = ["teacher_name", "details"]
    class LayeredTermScoreDetail(_message.Message):
        __slots__ = ["term", "is_hierarchy", "max", "min", "average", "num", "level1_num", "level2_num", "level3_num", "level4_num", "level5_num"]
        TERM_FIELD_NUMBER: _ClassVar[int]
        IS_HIERARCHY_FIELD_NUMBER: _ClassVar[int]
        MAX_FIELD_NUMBER: _ClassVar[int]
        MIN_FIELD_NUMBER: _ClassVar[int]
        AVERAGE_FIELD_NUMBER: _ClassVar[int]
        NUM_FIELD_NUMBER: _ClassVar[int]
        LEVEL1_NUM_FIELD_NUMBER: _ClassVar[int]
        LEVEL2_NUM_FIELD_NUMBER: _ClassVar[int]
        LEVEL3_NUM_FIELD_NUMBER: _ClassVar[int]
        LEVEL4_NUM_FIELD_NUMBER: _ClassVar[int]
        LEVEL5_NUM_FIELD_NUMBER: _ClassVar[int]
        term: _mycqu_model_pb2.CquSession
        is_hierarchy: bool
        max: float
        min: float
        average: float
        num: int
        level1_num: int
        level2_num: int
        level3_num: int
        level4_num: int
        level5_num: int
        def __init__(self, term: _Optional[_Union[_mycqu_model_pb2.CquSession, _Mapping]] = ..., is_hierarchy: bool = ..., max: _Optional[float] = ..., min: _Optional[float] = ..., average: _Optional[float] = ..., num: _Optional[int] = ..., level1_num: _Optional[int] = ..., level2_num: _Optional[int] = ..., level3_num: _Optional[int] = ..., level4_num: _Optional[int] = ..., level5_num: _Optional[int] = ...) -> None: ...
    TEACHER_NAME_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    teacher_name: str
    details: _containers.RepeatedCompositeFieldContainer[LayeredScoreDetail.LayeredTermScoreDetail]
    def __init__(self, teacher_name: _Optional[str] = ..., details: _Optional[_Iterable[_Union[LayeredScoreDetail.LayeredTermScoreDetail, _Mapping]]] = ...) -> None: ...

class FetchLayeredScoreDetailResponse(_message.Message):
    __slots__ = ["course_name", "course_code", "score_details"]
    COURSE_NAME_FIELD_NUMBER: _ClassVar[int]
    COURSE_CODE_FIELD_NUMBER: _ClassVar[int]
    SCORE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    course_name: str
    course_code: str
    score_details: _containers.RepeatedCompositeFieldContainer[LayeredScoreDetail]
    def __init__(self, course_name: _Optional[str] = ..., course_code: _Optional[str] = ..., score_details: _Optional[_Iterable[_Union[LayeredScoreDetail, _Mapping]]] = ...) -> None: ...

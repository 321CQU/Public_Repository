from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Bill(_message.Message):
    __slots__ = ["acc_amount", "date", "name", "place", "tran_amount"]
    ACC_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PLACE_FIELD_NUMBER: _ClassVar[int]
    TRAN_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    acc_amount: float
    date: int
    name: str
    place: str
    tran_amount: float
    def __init__(self, name: _Optional[str] = ..., date: _Optional[int] = ..., place: _Optional[str] = ..., tran_amount: _Optional[float] = ..., acc_amount: _Optional[float] = ...) -> None: ...

class Card(_message.Message):
    __slots__ = ["amount", "id"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    amount: float
    id: str
    def __init__(self, id: _Optional[str] = ..., amount: _Optional[float] = ...) -> None: ...

class Course(_message.Message):
    __slots__ = ["code", "course_num", "credit", "dept", "instructor", "name", "session"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    COURSE_NUM_FIELD_NUMBER: _ClassVar[int]
    CREDIT_FIELD_NUMBER: _ClassVar[int]
    DEPT_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTOR_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    code: str
    course_num: str
    credit: float
    dept: str
    instructor: str
    name: str
    session: CquSession
    def __init__(self, name: _Optional[str] = ..., code: _Optional[str] = ..., course_num: _Optional[str] = ..., dept: _Optional[str] = ..., credit: _Optional[float] = ..., instructor: _Optional[str] = ..., session: _Optional[_Union[CquSession, _Mapping]] = ...) -> None: ...

class CourseDayTime(_message.Message):
    __slots__ = ["period", "weekday"]
    PERIOD_FIELD_NUMBER: _ClassVar[int]
    WEEKDAY_FIELD_NUMBER: _ClassVar[int]
    period: Period
    weekday: int
    def __init__(self, weekday: _Optional[int] = ..., period: _Optional[_Union[Period, _Mapping]] = ...) -> None: ...

class CourseTimetable(_message.Message):
    __slots__ = ["classroom", "classroom_name", "course", "day_time", "expr_projects", "stu_num", "weeks", "whole_week"]
    CLASSROOM_FIELD_NUMBER: _ClassVar[int]
    CLASSROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    COURSE_FIELD_NUMBER: _ClassVar[int]
    DAY_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPR_PROJECTS_FIELD_NUMBER: _ClassVar[int]
    STU_NUM_FIELD_NUMBER: _ClassVar[int]
    WEEKS_FIELD_NUMBER: _ClassVar[int]
    WHOLE_WEEK_FIELD_NUMBER: _ClassVar[int]
    classroom: str
    classroom_name: str
    course: Course
    day_time: CourseDayTime
    expr_projects: _containers.RepeatedScalarFieldContainer[str]
    stu_num: int
    weeks: _containers.RepeatedCompositeFieldContainer[Period]
    whole_week: bool
    def __init__(self, course: _Optional[_Union[Course, _Mapping]] = ..., stu_num: _Optional[int] = ..., classroom: _Optional[str] = ..., weeks: _Optional[_Iterable[_Union[Period, _Mapping]]] = ..., day_time: _Optional[_Union[CourseDayTime, _Mapping]] = ..., whole_week: bool = ..., classroom_name: _Optional[str] = ..., expr_projects: _Optional[_Iterable[str]] = ...) -> None: ...

class CquSession(_message.Message):
    __slots__ = ["id", "is_autumn", "year"]
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_AUTUMN_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    id: int
    is_autumn: bool
    year: int
    def __init__(self, id: _Optional[int] = ..., year: _Optional[int] = ..., is_autumn: bool = ...) -> None: ...

class CquSessionInfo(_message.Message):
    __slots__ = ["begin_date", "end_date", "session"]
    BEGIN_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    begin_date: int
    end_date: int
    session: CquSession
    def __init__(self, session: _Optional[_Union[CquSession, _Mapping]] = ..., begin_date: _Optional[int] = ..., end_date: _Optional[int] = ...) -> None: ...

class EnergyFees(_message.Message):
    __slots__ = ["balance", "electricity_subsidy", "subsidies", "water_subsidy"]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    ELECTRICITY_SUBSIDY_FIELD_NUMBER: _ClassVar[int]
    SUBSIDIES_FIELD_NUMBER: _ClassVar[int]
    WATER_SUBSIDY_FIELD_NUMBER: _ClassVar[int]
    balance: float
    electricity_subsidy: float
    subsidies: float
    water_subsidy: float
    def __init__(self, balance: _Optional[float] = ..., electricity_subsidy: _Optional[float] = ..., water_subsidy: _Optional[float] = ..., subsidies: _Optional[float] = ...) -> None: ...

class EnrollCourseInfo(_message.Message):
    __slots__ = ["campus", "category", "course", "course_nature", "enroll_sign", "id", "type"]
    CAMPUS_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    COURSE_FIELD_NUMBER: _ClassVar[int]
    COURSE_NATURE_FIELD_NUMBER: _ClassVar[int]
    ENROLL_SIGN_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    campus: _containers.RepeatedScalarFieldContainer[str]
    category: str
    course: Course
    course_nature: str
    enroll_sign: str
    id: str
    type: str
    def __init__(self, id: _Optional[str] = ..., course: _Optional[_Union[Course, _Mapping]] = ..., category: _Optional[str] = ..., type: _Optional[str] = ..., enroll_sign: _Optional[str] = ..., course_nature: _Optional[str] = ..., campus: _Optional[_Iterable[str]] = ...) -> None: ...

class EnrollCourseItem(_message.Message):
    __slots__ = ["campus", "capacity", "checked", "children", "course", "course_id", "id", "parent_id", "selected_num", "session_id", "timetables", "type"]
    CAMPUS_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    CHECKED_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    COURSE_FIELD_NUMBER: _ClassVar[int]
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    SELECTED_NUM_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TIMETABLES_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    campus: str
    capacity: int
    checked: bool
    children: _containers.RepeatedCompositeFieldContainer[EnrollCourseItem]
    course: Course
    course_id: str
    id: str
    parent_id: str
    selected_num: int
    session_id: str
    timetables: _containers.RepeatedCompositeFieldContainer[EnrollCourseTimetable]
    type: str
    def __init__(self, id: _Optional[str] = ..., session_id: _Optional[str] = ..., checked: bool = ..., course_id: _Optional[str] = ..., course: _Optional[_Union[Course, _Mapping]] = ..., type: _Optional[str] = ..., selected_num: _Optional[int] = ..., capacity: _Optional[int] = ..., children: _Optional[_Iterable[_Union[EnrollCourseItem, _Mapping]]] = ..., campus: _Optional[str] = ..., parent_id: _Optional[str] = ..., timetables: _Optional[_Iterable[_Union[EnrollCourseTimetable, _Mapping]]] = ...) -> None: ...

class EnrollCourseTimetable(_message.Message):
    __slots__ = ["pos", "time", "weeks"]
    POS_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    WEEKS_FIELD_NUMBER: _ClassVar[int]
    pos: str
    time: CourseDayTime
    weeks: _containers.RepeatedCompositeFieldContainer[Period]
    def __init__(self, weeks: _Optional[_Iterable[_Union[Period, _Mapping]]] = ..., time: _Optional[_Union[CourseDayTime, _Mapping]] = ..., pos: _Optional[str] = ...) -> None: ...

class Exam(_message.Message):
    __slots__ = ["asst_invi", "batch", "batch_id", "building", "chief_invi", "course", "date", "end_time", "floor", "room", "seat_num", "start_time", "stu_id", "stu_num", "week", "weekday"]
    ASST_INVI_FIELD_NUMBER: _ClassVar[int]
    BATCH_FIELD_NUMBER: _ClassVar[int]
    BATCH_ID_FIELD_NUMBER: _ClassVar[int]
    BUILDING_FIELD_NUMBER: _ClassVar[int]
    CHIEF_INVI_FIELD_NUMBER: _ClassVar[int]
    COURSE_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    FLOOR_FIELD_NUMBER: _ClassVar[int]
    ROOM_FIELD_NUMBER: _ClassVar[int]
    SEAT_NUM_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    STU_ID_FIELD_NUMBER: _ClassVar[int]
    STU_NUM_FIELD_NUMBER: _ClassVar[int]
    WEEKDAY_FIELD_NUMBER: _ClassVar[int]
    WEEK_FIELD_NUMBER: _ClassVar[int]
    asst_invi: _containers.RepeatedCompositeFieldContainer[Invigilator]
    batch: str
    batch_id: int
    building: str
    chief_invi: _containers.RepeatedCompositeFieldContainer[Invigilator]
    course: Course
    date: str
    end_time: str
    floor: int
    room: str
    seat_num: int
    start_time: str
    stu_id: str
    stu_num: int
    week: int
    weekday: int
    def __init__(self, course: _Optional[_Union[Course, _Mapping]] = ..., batch: _Optional[str] = ..., batch_id: _Optional[int] = ..., building: _Optional[str] = ..., floor: _Optional[int] = ..., room: _Optional[str] = ..., stu_num: _Optional[int] = ..., date: _Optional[str] = ..., start_time: _Optional[str] = ..., end_time: _Optional[str] = ..., week: _Optional[int] = ..., weekday: _Optional[int] = ..., stu_id: _Optional[str] = ..., seat_num: _Optional[int] = ..., chief_invi: _Optional[_Iterable[_Union[Invigilator, _Mapping]]] = ..., asst_invi: _Optional[_Iterable[_Union[Invigilator, _Mapping]]] = ...) -> None: ...

class GpaRanking(_message.Message):
    __slots__ = ["class_ranking", "gpa", "grade_ranking", "major_ranking", "minor_gpa", "minor_weighted_avg", "weighted_avg"]
    CLASS_RANKING_FIELD_NUMBER: _ClassVar[int]
    GPA_FIELD_NUMBER: _ClassVar[int]
    GRADE_RANKING_FIELD_NUMBER: _ClassVar[int]
    MAJOR_RANKING_FIELD_NUMBER: _ClassVar[int]
    MINOR_GPA_FIELD_NUMBER: _ClassVar[int]
    MINOR_WEIGHTED_AVG_FIELD_NUMBER: _ClassVar[int]
    WEIGHTED_AVG_FIELD_NUMBER: _ClassVar[int]
    class_ranking: int
    gpa: float
    grade_ranking: int
    major_ranking: int
    minor_gpa: float
    minor_weighted_avg: float
    weighted_avg: float
    def __init__(self, gpa: _Optional[float] = ..., weighted_avg: _Optional[float] = ..., minor_gpa: _Optional[float] = ..., minor_weighted_avg: _Optional[float] = ..., major_ranking: _Optional[int] = ..., grade_ranking: _Optional[int] = ..., class_ranking: _Optional[int] = ...) -> None: ...

class Invigilator(_message.Message):
    __slots__ = ["dept", "name"]
    DEPT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    dept: str
    name: str
    def __init__(self, name: _Optional[str] = ..., dept: _Optional[str] = ...) -> None: ...

class Period(_message.Message):
    __slots__ = ["end", "start"]
    END_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    end: int
    start: int
    def __init__(self, start: _Optional[int] = ..., end: _Optional[int] = ...) -> None: ...

class Score(_message.Message):
    __slots__ = ["course", "course_nature", "score", "session", "study_nature"]
    COURSE_FIELD_NUMBER: _ClassVar[int]
    COURSE_NATURE_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    STUDY_NATURE_FIELD_NUMBER: _ClassVar[int]
    course: Course
    course_nature: str
    score: str
    session: CquSession
    study_nature: str
    def __init__(self, session: _Optional[_Union[CquSession, _Mapping]] = ..., course: _Optional[_Union[Course, _Mapping]] = ..., score: _Optional[str] = ..., study_nature: _Optional[str] = ..., course_nature: _Optional[str] = ...) -> None: ...

class UserInfo(_message.Message):
    __slots__ = ["code", "email", "id", "name", "phone_number", "role"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    code: str
    email: str
    id: str
    name: str
    phone_number: str
    role: str
    def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ..., code: _Optional[str] = ..., role: _Optional[str] = ..., email: _Optional[str] = ..., phone_number: _Optional[str] = ...) -> None: ...

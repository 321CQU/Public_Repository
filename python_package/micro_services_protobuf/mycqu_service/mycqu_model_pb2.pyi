from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Period(_message.Message):
    __slots__ = ["start", "end"]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    start: int
    end: int
    def __init__(self, start: _Optional[int] = ..., end: _Optional[int] = ...) -> None: ...

class UserInfo(_message.Message):
    __slots__ = ["name", "id", "code", "role", "email", "phone_number"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    code: str
    role: str
    email: str
    phone_number: str
    def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ..., code: _Optional[str] = ..., role: _Optional[str] = ..., email: _Optional[str] = ..., phone_number: _Optional[str] = ...) -> None: ...

class Bill(_message.Message):
    __slots__ = ["name", "date", "place", "tran_amount", "acc_amount"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    PLACE_FIELD_NUMBER: _ClassVar[int]
    TRAN_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    ACC_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    name: str
    date: int
    place: str
    tran_amount: float
    acc_amount: float
    def __init__(self, name: _Optional[str] = ..., date: _Optional[int] = ..., place: _Optional[str] = ..., tran_amount: _Optional[float] = ..., acc_amount: _Optional[float] = ...) -> None: ...

class Card(_message.Message):
    __slots__ = ["id", "amount"]
    ID_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    amount: float
    def __init__(self, id: _Optional[str] = ..., amount: _Optional[float] = ...) -> None: ...

class EnergyFees(_message.Message):
    __slots__ = ["balance", "electricity_subsidy", "water_subsidy", "subsidies"]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    ELECTRICITY_SUBSIDY_FIELD_NUMBER: _ClassVar[int]
    WATER_SUBSIDY_FIELD_NUMBER: _ClassVar[int]
    SUBSIDIES_FIELD_NUMBER: _ClassVar[int]
    balance: float
    electricity_subsidy: float
    water_subsidy: float
    subsidies: float
    def __init__(self, balance: _Optional[float] = ..., electricity_subsidy: _Optional[float] = ..., water_subsidy: _Optional[float] = ..., subsidies: _Optional[float] = ...) -> None: ...

class CquSession(_message.Message):
    __slots__ = ["id", "year", "is_autumn"]
    ID_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    IS_AUTUMN_FIELD_NUMBER: _ClassVar[int]
    id: int
    year: int
    is_autumn: bool
    def __init__(self, id: _Optional[int] = ..., year: _Optional[int] = ..., is_autumn: bool = ...) -> None: ...

class CquSessionInfo(_message.Message):
    __slots__ = ["session", "begin_date", "end_date"]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    BEGIN_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    session: CquSession
    begin_date: int
    end_date: int
    def __init__(self, session: _Optional[_Union[CquSession, _Mapping]] = ..., begin_date: _Optional[int] = ..., end_date: _Optional[int] = ...) -> None: ...

class Course(_message.Message):
    __slots__ = ["name", "code", "course_num", "dept", "credit", "instructor", "session"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    COURSE_NUM_FIELD_NUMBER: _ClassVar[int]
    DEPT_FIELD_NUMBER: _ClassVar[int]
    CREDIT_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTOR_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    code: str
    course_num: str
    dept: str
    credit: float
    instructor: str
    session: CquSession
    def __init__(self, name: _Optional[str] = ..., code: _Optional[str] = ..., course_num: _Optional[str] = ..., dept: _Optional[str] = ..., credit: _Optional[float] = ..., instructor: _Optional[str] = ..., session: _Optional[_Union[CquSession, _Mapping]] = ...) -> None: ...

class CourseDayTime(_message.Message):
    __slots__ = ["weekday", "period"]
    WEEKDAY_FIELD_NUMBER: _ClassVar[int]
    PERIOD_FIELD_NUMBER: _ClassVar[int]
    weekday: int
    period: Period
    def __init__(self, weekday: _Optional[int] = ..., period: _Optional[_Union[Period, _Mapping]] = ...) -> None: ...

class CourseTimetable(_message.Message):
    __slots__ = ["course", "stu_num", "classroom", "weeks", "day_time", "whole_week", "classroom_name", "expr_projects"]
    COURSE_FIELD_NUMBER: _ClassVar[int]
    STU_NUM_FIELD_NUMBER: _ClassVar[int]
    CLASSROOM_FIELD_NUMBER: _ClassVar[int]
    WEEKS_FIELD_NUMBER: _ClassVar[int]
    DAY_TIME_FIELD_NUMBER: _ClassVar[int]
    WHOLE_WEEK_FIELD_NUMBER: _ClassVar[int]
    CLASSROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    EXPR_PROJECTS_FIELD_NUMBER: _ClassVar[int]
    course: Course
    stu_num: int
    classroom: str
    weeks: _containers.RepeatedCompositeFieldContainer[Period]
    day_time: CourseDayTime
    whole_week: bool
    classroom_name: str
    expr_projects: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, course: _Optional[_Union[Course, _Mapping]] = ..., stu_num: _Optional[int] = ..., classroom: _Optional[str] = ..., weeks: _Optional[_Iterable[_Union[Period, _Mapping]]] = ..., day_time: _Optional[_Union[CourseDayTime, _Mapping]] = ..., whole_week: bool = ..., classroom_name: _Optional[str] = ..., expr_projects: _Optional[_Iterable[str]] = ...) -> None: ...

class EnrollCourseInfo(_message.Message):
    __slots__ = ["id", "course", "category", "type", "enroll_sign", "course_nature", "campus"]
    ID_FIELD_NUMBER: _ClassVar[int]
    COURSE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ENROLL_SIGN_FIELD_NUMBER: _ClassVar[int]
    COURSE_NATURE_FIELD_NUMBER: _ClassVar[int]
    CAMPUS_FIELD_NUMBER: _ClassVar[int]
    id: str
    course: Course
    category: str
    type: str
    enroll_sign: str
    course_nature: str
    campus: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., course: _Optional[_Union[Course, _Mapping]] = ..., category: _Optional[str] = ..., type: _Optional[str] = ..., enroll_sign: _Optional[str] = ..., course_nature: _Optional[str] = ..., campus: _Optional[_Iterable[str]] = ...) -> None: ...

class EnrollCourseTimetable(_message.Message):
    __slots__ = ["weeks", "time", "pos"]
    WEEKS_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    weeks: _containers.RepeatedCompositeFieldContainer[Period]
    time: CourseDayTime
    pos: str
    def __init__(self, weeks: _Optional[_Iterable[_Union[Period, _Mapping]]] = ..., time: _Optional[_Union[CourseDayTime, _Mapping]] = ..., pos: _Optional[str] = ...) -> None: ...

class EnrollCourseItem(_message.Message):
    __slots__ = ["id", "session_id", "checked", "course_id", "course", "type", "selected_num", "capacity", "children", "campus", "parent_id", "timetables"]
    ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    CHECKED_FIELD_NUMBER: _ClassVar[int]
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    COURSE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SELECTED_NUM_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    CAMPUS_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    TIMETABLES_FIELD_NUMBER: _ClassVar[int]
    id: str
    session_id: str
    checked: bool
    course_id: str
    course: Course
    type: str
    selected_num: int
    capacity: int
    children: _containers.RepeatedCompositeFieldContainer[EnrollCourseItem]
    campus: str
    parent_id: str
    timetables: _containers.RepeatedCompositeFieldContainer[EnrollCourseTimetable]
    def __init__(self, id: _Optional[str] = ..., session_id: _Optional[str] = ..., checked: bool = ..., course_id: _Optional[str] = ..., course: _Optional[_Union[Course, _Mapping]] = ..., type: _Optional[str] = ..., selected_num: _Optional[int] = ..., capacity: _Optional[int] = ..., children: _Optional[_Iterable[_Union[EnrollCourseItem, _Mapping]]] = ..., campus: _Optional[str] = ..., parent_id: _Optional[str] = ..., timetables: _Optional[_Iterable[_Union[EnrollCourseTimetable, _Mapping]]] = ...) -> None: ...

class Invigilator(_message.Message):
    __slots__ = ["name", "dept"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEPT_FIELD_NUMBER: _ClassVar[int]
    name: str
    dept: str
    def __init__(self, name: _Optional[str] = ..., dept: _Optional[str] = ...) -> None: ...

class Exam(_message.Message):
    __slots__ = ["course", "batch", "batch_id", "building", "floor", "room", "stu_num", "date", "start_time", "end_time", "week", "weekday", "stu_id", "seat_num", "chief_invi", "asst_invi"]
    COURSE_FIELD_NUMBER: _ClassVar[int]
    BATCH_FIELD_NUMBER: _ClassVar[int]
    BATCH_ID_FIELD_NUMBER: _ClassVar[int]
    BUILDING_FIELD_NUMBER: _ClassVar[int]
    FLOOR_FIELD_NUMBER: _ClassVar[int]
    ROOM_FIELD_NUMBER: _ClassVar[int]
    STU_NUM_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    WEEK_FIELD_NUMBER: _ClassVar[int]
    WEEKDAY_FIELD_NUMBER: _ClassVar[int]
    STU_ID_FIELD_NUMBER: _ClassVar[int]
    SEAT_NUM_FIELD_NUMBER: _ClassVar[int]
    CHIEF_INVI_FIELD_NUMBER: _ClassVar[int]
    ASST_INVI_FIELD_NUMBER: _ClassVar[int]
    course: Course
    batch: str
    batch_id: int
    building: str
    floor: int
    room: str
    stu_num: int
    date: str
    start_time: str
    end_time: str
    week: int
    weekday: int
    stu_id: str
    seat_num: int
    chief_invi: _containers.RepeatedCompositeFieldContainer[Invigilator]
    asst_invi: _containers.RepeatedCompositeFieldContainer[Invigilator]
    def __init__(self, course: _Optional[_Union[Course, _Mapping]] = ..., batch: _Optional[str] = ..., batch_id: _Optional[int] = ..., building: _Optional[str] = ..., floor: _Optional[int] = ..., room: _Optional[str] = ..., stu_num: _Optional[int] = ..., date: _Optional[str] = ..., start_time: _Optional[str] = ..., end_time: _Optional[str] = ..., week: _Optional[int] = ..., weekday: _Optional[int] = ..., stu_id: _Optional[str] = ..., seat_num: _Optional[int] = ..., chief_invi: _Optional[_Iterable[_Union[Invigilator, _Mapping]]] = ..., asst_invi: _Optional[_Iterable[_Union[Invigilator, _Mapping]]] = ...) -> None: ...

class Score(_message.Message):
    __slots__ = ["session", "course", "score", "study_nature", "course_nature"]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    COURSE_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    STUDY_NATURE_FIELD_NUMBER: _ClassVar[int]
    COURSE_NATURE_FIELD_NUMBER: _ClassVar[int]
    session: CquSession
    course: Course
    score: str
    study_nature: str
    course_nature: str
    def __init__(self, session: _Optional[_Union[CquSession, _Mapping]] = ..., course: _Optional[_Union[Course, _Mapping]] = ..., score: _Optional[str] = ..., study_nature: _Optional[str] = ..., course_nature: _Optional[str] = ...) -> None: ...

class GpaRanking(_message.Message):
    __slots__ = ["gpa", "weighted_avg", "minor_gpa", "minor_weighted_avg", "major_ranking", "grade_ranking", "class_ranking"]
    GPA_FIELD_NUMBER: _ClassVar[int]
    WEIGHTED_AVG_FIELD_NUMBER: _ClassVar[int]
    MINOR_GPA_FIELD_NUMBER: _ClassVar[int]
    MINOR_WEIGHTED_AVG_FIELD_NUMBER: _ClassVar[int]
    MAJOR_RANKING_FIELD_NUMBER: _ClassVar[int]
    GRADE_RANKING_FIELD_NUMBER: _ClassVar[int]
    CLASS_RANKING_FIELD_NUMBER: _ClassVar[int]
    gpa: float
    weighted_avg: float
    minor_gpa: float
    minor_weighted_avg: float
    major_ranking: int
    grade_ranking: int
    class_ranking: int
    def __init__(self, gpa: _Optional[float] = ..., weighted_avg: _Optional[float] = ..., minor_gpa: _Optional[float] = ..., minor_weighted_avg: _Optional[float] = ..., major_ranking: _Optional[int] = ..., grade_ranking: _Optional[int] = ..., class_ranking: _Optional[int] = ...) -> None: ...

class BookInfo(_message.Message):
    __slots__ = ["id", "title", "call_no", "library_name", "borrow_time", "should_return_time", "is_return", "return_time", "renew_count", "can_renew"]
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CALL_NO_FIELD_NUMBER: _ClassVar[int]
    LIBRARY_NAME_FIELD_NUMBER: _ClassVar[int]
    BORROW_TIME_FIELD_NUMBER: _ClassVar[int]
    SHOULD_RETURN_TIME_FIELD_NUMBER: _ClassVar[int]
    IS_RETURN_FIELD_NUMBER: _ClassVar[int]
    RETURN_TIME_FIELD_NUMBER: _ClassVar[int]
    RENEW_COUNT_FIELD_NUMBER: _ClassVar[int]
    CAN_RENEW_FIELD_NUMBER: _ClassVar[int]
    id: int
    title: str
    call_no: str
    library_name: str
    borrow_time: int
    should_return_time: str
    is_return: bool
    return_time: str
    renew_count: int
    can_renew: bool
    def __init__(self, id: _Optional[int] = ..., title: _Optional[str] = ..., call_no: _Optional[str] = ..., library_name: _Optional[str] = ..., borrow_time: _Optional[int] = ..., should_return_time: _Optional[str] = ..., is_return: bool = ..., return_time: _Optional[str] = ..., renew_count: _Optional[int] = ..., can_renew: bool = ...) -> None: ...

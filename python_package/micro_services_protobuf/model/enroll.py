from typing import List, Optional

from pydantic import BaseModel, Field

from .course import Course, CourseDayTime
from .period import Period

__all__ = ['EnrollCourseInfo', 'EnrollCourseItem', 'EnrollCourseTimetable']


class EnrollCourseInfo(BaseModel):
    """
    可选课程信息
    """
    id: str = Field(title="可选课程id")
    """可选课程id"""
    course: Course = Field(title="可选课程信息")
    """可选课程信息"""
    category: str = Field(title="可选课程类型", description="公共基础课，主修专业课，非限制选修课等")
    """可选课程类型，如：公共基础课，主修专业课，非限制选修课等"""
    type: str = Field(title="课程类别", description="主修专业课，通识教育课程等")
    """课程类别，如：主修专业课，通识教育课程等"""
    enroll_sign: Optional[str] = Field(title="选课标识", description="已选，已选满等")
    """选课标识，如：已选，已选满等，当为 :obj:`None` 时标识无相关标记"""
    course_nature: str = Field(title="课程属性", description="必修，选修等")
    """课程属性，如必修，选修等"""
    campus: List[str] = Field(title="可选校区", description="如['D区'], ['A区', 'D区']等")
    """可选课程可选校区，如['D区'], ['A区', 'D区']等"""

    class Config:
        title = "可选课程信息"


class EnrollCourseTimetable(BaseModel):
    """
    可选具体课程上课时间、上课地点信息
    """
    weeks: List[Period] = Field(title="上课周数")
    """上课周数"""
    time: Optional[CourseDayTime] = Field(title="上课时间")
    """上课时间"""
    pos: Optional[str] = Field(title="上课地点")
    """上课地点"""

    class Config:
        title = "可选具体课程上课时间、上课地点信息"


class EnrollCourseItem(BaseModel):
    """
    可选具体课程，包含课程上课时间、上课教师、教室可容纳学生等信息
    """
    id: Optional[str] = Field(title="可选具体课程id", description="每个可选具体课程具有唯一id，部分从属课程该值为`None`")
    """可选具体课程id，每个可选具体课程具有唯一id，部分从属课程该值为`None`"""
    session_id: Optional[str] = Field(title="可选具体课程所在学期ID", description="部分从属课程该值为`None`")
    """可选具体课程所在学期ID，部分从属课程该值为`None`"""
    checked: Optional[bool] = Field(title="是否已经选择该课程", description="部分从属课程该值为`None`")
    """是否已经选择该课程，部分从属课程该值为`None`"""
    course_id: Optional[str] = Field(title="该具体课程所属课程ID", description="部分从属课程该值为`None`")
    """该具体课程所属课程ID，部分从属课程该值为`None`"""
    course: Course = Field(title="课程信息")
    """课程信息"""
    type: str = Field(title="具体课程类别", description="理论、实验")
    """具体课程类别，如：理论、实验"""
    selected_num: Optional[int] = Field(title="已选课程学生", description="部分从属课程该值为`None`")
    """已选课程学生，部分从属课程该值为`None`"""
    capacity: Optional[int] = Field(title="该课程容量上限", description="部分从属课程该值为`None`")
    """该课程容量上限，部分从属课程该值为`None`"""
    children: Optional[List["EnrollCourseItem"]] = Field(title="该课程从属课程列表", description="一般为理论课程的实验课")
    """该课程从属课程列表，一般为理论课程的实验课"""
    campus: Optional[str] = Field(title="所属校区", description="如D区，部分从属课程该值为`None`")
    """所属校区，如D区，部分从属课程该值为`None`"""
    parent_id: Optional[str] = Field(title="所从属具体课程id", description="如果不存在从属关系，该值为None")
    """所从属具体课程id，如果不存在从属关系，该值为None"""
    timetables: List[EnrollCourseTimetable] = Field(title="具体课程上课时间表")
    """具体课程上课时间表"""

    class Config:
        title = "可选具体课程，包含课程上课时间、上课教师、教室可容纳学生等信息"

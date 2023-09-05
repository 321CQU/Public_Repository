from typing import Optional, List

from pydantic import BaseModel, Field, ConfigDict

from .cqu_session import CQUSession
from .period import Period


__all__ = ['Course', 'CourseDayTime', 'CourseTimetable']


class Course(BaseModel):
    """
    与具体行课时间无关的课程信息
    """
    name: Optional[str] = Field(default=None, title="课程名称")
    """课程名称"""
    code: Optional[str] = Field(default=None, title="课程代码")
    """课程代码"""
    course_num: Optional[str] = Field(default=None, title="教学班号", description="在无法获取时（如考表Exam中）为None")
    """教学班号，在无法获取时（如考表 :class:`.exam.Exam` 中）设为 :obj:`None`"""
    dept: Optional[str] = Field(default=None, title="开课学院", description="在无法获取时（如成绩Score中）为None")
    """开课学院， 在无法获取时（如成绩 :class:`.score.Score`中）设为 :obj:`None`"""
    credit: Optional[float] = Field(default=None, title="学分", description="在无法获取时（如考表Exam中）为None")
    """学分，无法获取到则为 :obj:`None`（如在考表 :class:`.exam.Exam` 中）"""
    instructor: Optional[str] = Field(default=None, title="教师")
    """教师"""
    session: Optional[CQUSession] = Field(default=None, title="学期", description="在无法获取时为None")
    """学期，无法获取时则为 :obj:`None`"""

    model_config = ConfigDict(title="与具体行课时间无关的课程信息")


class CourseDayTime(BaseModel):
    """
    课程一次的星期和节次
    """
    weekday: int = Field(title="星期", description="0 为周一，6 为周日")
    """星期，0 为周一，6 为周日，此与 :attr:`datetime.date.day` 一致"""
    period: Period = Field(title="节次")
    """
    节次，第一个元素为开始节次，第二个元素为结束节次（该节次也包括在范围内）。
    只有一节课时，两个元素相同。
    """

    model_config = ConfigDict(title="课程一次的星期和节次")


class CourseTimetable(BaseModel):
    """
    课表对象，一个对象存储有相同课程、相同行课节次和相同星期的一批行课安排
    """
    course: Course = Field(title="对应的课程")
    """对应的课程"""
    stu_num: Optional[int] = Field(default=None, title="学生数")
    """学生数"""
    classroom: Optional[str] = Field(default=None, title="行课地点")
    """行课地点，无则为 :obj:`None`"""
    weeks: List[Period] = Field(title="行课周数")
    """行课周数，列表中每个元组 (a,b) 代表一个周数范围 a~b（包含 a, b），在单独的一周则有 b=a"""
    day_time: Optional[CourseDayTime] = Field(
        default=None, title="行课的星期和节次",
        description="若时间是整周（如真实地占用整周的军训和某些实习、虚拟地使用一周的思修实践）则为None"
    )
    """行课的星期和节次，若时间是整周（如真实地占用整周的军训和某些实习、虚拟地使用一周的思修实践）
    则为 :obj:`None`"""
    whole_week: bool = Field(title="是否真实地占用整周", description="如军训和某些实习是真实地占用、思修实践是“虚拟地占用”")
    """是否真实地占用整周（如军训和某些实习是真实地占用、思修实践是“虚拟地占用”）"""
    classroom_name: Optional[str] = Field(default=None, title="行课教室名称")
    """行课教室名称"""
    expr_projects: List[str] = Field(title="实验课各次实验内容")
    """实验课各次实验内容"""

    model_config = ConfigDict(title="课表对象，一个对象存储有相同课程、相同行课节次和相同星期的一批行课安排")

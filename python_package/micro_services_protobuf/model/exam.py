from typing import Optional, List
import datetime

from pydantic import BaseModel, Field

from .course import Course

__all__ = ['Exam', 'Invigilator']


class Invigilator(BaseModel):
    """
    监考员信息
    """
    name: str = Field(title="监考员姓名")
    """监考员姓名"""
    dept: str = Field(title="监考员所在学院")
    """监考员所在学院（可能是简称，如 数统）"""

    class Config:
        title = "监考员信息"


class Exam(BaseModel):
    """
    考试信息
    """
    course: Course = Field(
        title="考试对应的课程", description="学分`credit`、教师`instructor`、教学班号`course_num` 可能无法获取（其值会设置为`None`）"
    )
    """考试对应的课程，其中学分 :attr:`credit`、教师 :attr:`instructor`、教学班号 :attr:`course_num` 可能无法获取（其值会设置为 :obj:`None`）"""
    batch: str = Field(title="考试批次", description="如: 非集中考试周")
    """考试批次，如 :obj:`"非集中考试周"`"""
    batch_id: int = Field(title="选课系统中考试批次的内部id")
    """选课系统中考试批次的内部id"""
    building: str = Field(title="考场楼栋")
    """考场楼栋"""
    floor: int = Field(title="考场楼层")
    """考场楼层"""
    room: str = Field(title="考场地点")
    """考场地点"""
    stu_num: int = Field(title="考场人数")
    """考场人数"""
    date: datetime.date = Field(title="考试日期")
    """考试日期"""
    start_time: datetime.time = Field(title="考试开始时间")
    """考试开始时间"""
    end_time: datetime.time = Field(title="考试结束时间")
    """考试结束时间"""
    week: int = Field(title="周次")
    """周次"""
    weekday: int = Field(title="星期", description="0为周一，6为周日")
    """星期，0为周一，6为周日"""
    stu_id: str = Field(title="考生学号")
    """考生学号"""
    seat_num: int = Field(title="考生座号")
    """考生座号"""
    chief_invi: List[Invigilator] = Field(title="监考员")
    """监考员"""
    asst_invi: Optional[List[Invigilator]] = Field(title="副监考员")
    """副监考员"""

    class Config:
        title = "考试信息"

from typing import Optional

from pydantic import BaseModel, Field, ConfigDict

from .course import Course
from .cqu_session import CQUSession

__all__ = ['Score', 'GpaRanking']


class Score(BaseModel):
    """
    成绩对象
    """
    session: CQUSession = Field(title="学期")
    """学期"""
    course: Course = Field(title="课程")
    """课程"""
    score: Optional[str] = Field(default=None, title="成绩", description="可能为数字，也可能为字符（优、良等）")
    """成绩，可能为数字，也可能为字符（优、良等）"""
    study_nature: str = Field(title="初修/重修")
    """初修/重修"""
    course_nature: str = Field(title="必修/选修")
    """必修/选修"""

    model_config = ConfigDict(title="成绩对象")


class GpaRanking(BaseModel):
    """
    绩点对象
    """
    gpa: float = Field(title="学生总绩点")
    """学生总绩点"""
    major_ranking: Optional[int] = Field(default=None, title="专业排名")
    """专业排名"""
    grade_ranking: Optional[int] = Field(default=None, title="年级排名")
    """年级排名"""
    class_ranking: Optional[int] = Field(default=None, title="班级排名")
    """班级排名"""
    weighted_avg: float = Field(default=None, title="加权平均分")
    """加权平均分"""
    minor_weighted_avg: Optional[float] = Field(default=None, title="辅修加权平均分")
    """辅修加权平均分"""
    minor_gpa: Optional[float] = Field(default=None, title="辅修绩点")
    """辅修绩点"""

    model_config = ConfigDict(title="绩点对象")

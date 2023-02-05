from typing import Optional

from pydantic import BaseModel, Field

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
    score: Optional[str] = Field(title="成绩", description="可能为数字，也可能为字符（优、良等）")
    """成绩，可能为数字，也可能为字符（优、良等）"""
    study_nature: str = Field(title="初修/重修")
    """初修/重修"""
    course_nature: str = Field(title="必修/选修")
    """必修/选修"""

    class Config:
        title = "成绩对象"


class GpaRanking(BaseModel):
    """
    绩点对象
    """
    gpa: float = Field(title="学生总绩点")
    """学生总绩点"""
    majorRanking: Optional[int] = Field(title="专业排名")
    """专业排名"""
    gradeRanking: Optional[int] = Field(title="年级排名")
    """年级排名"""
    classRanking: Optional[int] = Field(title="班级排名")
    """班级排名"""
    weightedAvg: float = Field(title="加权平均分")
    """加权平均分"""
    minorWeightedAvg: Optional[float] = Field(title="辅修加权平均分")
    """辅修加权平均分"""
    minorGpa: Optional[float] = Field(title="辅修绩点")
    """辅修绩点"""

    class Config:
        title = "绩点对象"

from pydantic import BaseModel, Field, ConfigDict

__all__ = ['Period']


class Period(BaseModel):
    """
    时间段，用于课程节数、周数区间等
    """
    start: int = Field(title="起始值")
    """起始值"""
    end: int = Field(title="终止值")
    """终止值"""

    model_config = ConfigDict(title="时间段")

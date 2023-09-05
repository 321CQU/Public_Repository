import re
from datetime import date
from typing import ClassVar, Tuple, Optional

from pydantic import BaseModel, Field, ConfigDict

__all__ = ['CQUSession', 'CQUSessionInfo']


SESSION_RE: ClassVar = re.compile("^([0-9]{4})年?(春|秋)$")
_SPECIAL_IDS: ClassVar[Tuple[int, ...]] = (
    239259, 102, 101, 103, 1028, 1029, 1030, 1032)  # 2015 ~ 2018


class CQUSession(BaseModel):
    """
    重大的某一学期
    """
    id: Optional[int] = Field(default=None, title="学期ID")
    """学期ID"""
    year: int = Field(title="主要行课年份")
    """主要行课年份"""
    is_autumn: bool = Field(title="是否为秋冬季学期")
    """是否为秋冬季学期"""

    model_config = ConfigDict(title="重大的某一学期")

    def __str__(self):
        return str(self.year) + ('秋' if self.is_autumn else '春')


class CQUSessionInfo(BaseModel):
    """
    某学期的一些额外信息
    """
    session: CQUSession = Field(title="对应的学期")
    """对应的学期"""
    begin_date: Optional[date] = Field(default=None, title="学期的开始日期")
    """学期的开始日期"""
    end_date: Optional[date] = Field(default=None, title="学期的结束日期")
    """学期的结束日期"""

    model_config = ConfigDict(title="某学期的一些额外信息")

import re
from datetime import date
from typing import ClassVar, Tuple, Optional

from pydantic import BaseModel, Field

__all__ = ['CQUSession', 'CQUSessionInfo']


SESSION_RE: ClassVar = re.compile("^([0-9]{4})年?(春|秋)$")
_SPECIAL_IDS: ClassVar[Tuple[int, ...]] = (
    239259, 102, 101, 103, 1028, 1029, 1030, 1032)  # 2015 ~ 2018


class CQUSession(BaseModel):
    """
    重大的某一学期
    """
    year: int = Field(title="主要行课年份")
    """主要行课年份"""
    is_autumn: bool = Field(title="是否为秋冬季学期")
    """是否为秋冬季学期"""

    class Config:
        title = "重大的某一学期"

    def __str__(self):
        return str(self.year) + ('秋' if self.is_autumn else '春')

    def get_id(self) -> int:
        """获取该学期在 my.cqu.edu.cn 中的 id

        >>> CQUSession(2021, True).get_id()
        1038

        :return: 学期的 id
        :rtype: int
        """
        if self.year >= 2019:
            return (self.year - 1503) * 2 + int(self.is_autumn) + 1
        elif 2015 <= self.year <= 2018:
            return _SPECIAL_IDS[(self.year - 2015) * 2 + int(self.is_autumn)]
        else:
            return (2015 - self.year) * 2 - int(self.is_autumn)

    @staticmethod
    def from_str(string: str) -> "CQUSession":
        """从学期字符串中解析学期

        >>> CQUSession.from_str("2021春")
        CQUSession(year=2021, is_autumn=False)
        >>> CQUSession.from_str("2020年秋")
        CQUSession(year=2020, is_autumn=True)

        :param string: 学期字符串，如“2021春”、“2020年秋”
        :type string: str
        :raises ValueError: 字符串不是一个预期中的学期字符串时抛出
        :return: 对应的学期
        :rtype: CQUSession
        """
        match = SESSION_RE.match(string)
        if match:
            return CQUSession(
                year=match[1],
                is_autumn=match[2] == "秋"
            )
        else:
            raise ValueError(f"string {string} is not a session")


class CQUSessionInfo(BaseModel):
    """
    某学期的一些额外信息
    """
    session: CQUSession = Field(title="对应的学期")
    """对应的学期"""
    begin_date: Optional[date] = Field(title="学期的开始日期")
    """学期的开始日期"""
    end_date: Optional[date] = Field(title="学期的结束日期")
    """学期的结束日期"""

    class Config:
        title = "某学期的一些额外信息"

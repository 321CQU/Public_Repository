from datetime import datetime, date
from typing import Optional

from pydantic import BaseModel, Field


class BookInfo(BaseModel):
    """
    图书馆书籍相关信息
    """
    id: Optional[int] = Field(title="书籍id")
    """书籍id"""
    title: str = Field(title="书籍名称")
    """书籍名称"""
    call_no: str = Field(title="书籍检索号")
    """书籍检索号"""
    library_name: str = Field(title="所属图书馆（如虎溪图书馆自然科学阅览室等）")
    """所属图书馆（如虎溪图书馆自然科学阅览室等）"""
    borrow_time: datetime = Field(title="借出时间")
    """借出时间"""
    should_return_time: Optional[date] = Field(title="应归还日期")
    """应归还日期"""
    is_return: bool = Field(title="是否被归还")
    """是否被归还"""
    return_time: Optional[date] = Field(title="归还时间")
    """归还时间"""
    renew_count: int = Field(title="续借次数")
    """续借次数"""
    can_renew: bool = Field(title="是否可被续借")
    """是否可被续借"""

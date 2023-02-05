from pydantic import BaseModel, Field

__all__ = ["User"]


class User(BaseModel):
    """用户信息"""

    name: str = Field(title="姓名")
    """姓名"""
    id: str = Field(title="统一身份认证号")
    """统一身份认证号"""
    code: str = Field(title="学工号")
    """学工号"""
    role: str = Field(title="身份", description="已知取值有学生 student、教师instructor")
    """身份，已知取值有学生 :obj:`"student"`、教师 :obj:`"instructor`"`"""
    email: str = Field(title="电子邮箱")
    "电子邮箱"
    phone_number: str = Field(title="电话号码")
    "电话号码"

    class Config:
        title = "用户信息"

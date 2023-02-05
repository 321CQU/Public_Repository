from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


__all__ = ['Card', 'Bill', 'EnergyFees']


class Card(BaseModel):
    """
    校园卡及其账单信息
    """
    id: str = Field(title="校园卡id")
    """校园卡id"""
    amount: float = Field(title="账户余额")
    """账户余额"""

    class Config:
        title = '校园卡及其账单信息'


class Bill(BaseModel):
    """
    某次消费账单信息
    """
    tran_name: str = Field(title="交易名称")
    """交易名称"""
    tran_date: datetime = Field(title="交易时间")
    """交易时间"""
    tran_place: str = Field(title="交易地点")
    """交易地点"""
    tran_amount: float = Field(title="交易金额")
    """交易金额"""
    acc_amount: float = Field(title="账户余额")
    """账户余额"""

    class Config:
        title = "某次消费账单信息"


class EnergyFees(BaseModel):
    """
    某宿舍的水电费相关信息
    """
    balance: float = Field(title="账户余额")
    """账户余额"""
    electricity_subsidy: Optional[float] = Field(title="电剩余补助（仅虎溪校区拥有）")
    """电剩余补助（仅虎溪校区拥有）"""
    water_subsidy: Optional[float] = Field(title="水剩余补助（仅虎溪校区拥有）")
    """水剩余补助（仅虎溪校区拥有）"""
    subsidies: Optional[float] = Field(title="补助余额（仅老校区拥有）")
    """补助余额（仅老校区拥有）"""

    class Config:
        title = "某宿舍的水电费相关信息"

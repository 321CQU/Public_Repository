from abc import ABC, abstractmethod
from typing import Iterable, Any

from .AbstractSql import AbstractConnection, AbstractAioCursor

__all__ = ['SqlManager']


class SqlManager(ABC):
    """
    抽象异步数据库管理类
    """

    @abstractmethod
    async def connect(self) -> AbstractConnection:
        pass

    @abstractmethod
    async def execute(self, sql: str, parameters: Iterable[Any] = None) -> AbstractAioCursor:
        pass

    @abstractmethod
    async def executemany(
            self, sql: str, parameters: Iterable[Iterable[Any]]
    ) -> AbstractAioCursor:
        pass

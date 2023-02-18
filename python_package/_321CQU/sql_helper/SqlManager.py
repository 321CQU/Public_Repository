from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict

from .AbstractSql import AbstractConnection, AbstractAioCursor
from ..tools.ConfigHandler import _CONFIG_HANDLER

__all__ = ['SqlManager', 'DatabaseConfig']


class DatabaseConfig(Enum):
    Notification = 'notice'
    User = 'user'
    Score = 'score'

    @property
    def host(self) -> str:
        return _CONFIG_HANDLER.get_config('DatabaseConfig', self.value + "_host")

    @property
    def port(self) -> int:
        return int(_CONFIG_HANDLER.get_config('DatabaseConfig', self.value + '_port'))

    @property
    def user(self) -> str:
        return _CONFIG_HANDLER.get_config('DatabaseConfig', self.value + '_user')

    @property
    def password(self) -> str:
        return _CONFIG_HANDLER.get_config('DatabaseConfig', self.value + '_password')

    @property
    def target_db(self) -> str:
        return _CONFIG_HANDLER.get_config('DatabaseConfig', self.value + '_target_database')

    @property
    def config_dict(self) -> Dict:
        return {
            'host': self.host,
            'port': self.port,
            'user': self.user,
            'password': self.password,
            'db': self.target_db
        }


class SqlManager(ABC):
    """
    抽象异步数据库管理类
    """

    @abstractmethod
    async def connect(self, config: DatabaseConfig, *args, **kwargs) -> AbstractConnection:
        pass

    @abstractmethod
    async def cursor(self, config: DatabaseConfig, *args, **kwargs) -> AbstractAioCursor:
        pass

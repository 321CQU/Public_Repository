from configparser import ConfigParser
from typing import List

from ..tools.Singleton import Singleton

__all__ = ['ConfigHandler']


class ConfigHandler(metaclass=Singleton):
    """
    单例模式实现的配置文件读取类
    """
    def __init__(self, path: str):
        """

        :param path: 日志文件路径
        """
        self._config_parser = ConfigParser()
        self._config_parser.read(path)

    def get_config(self, section: str, option: str) -> str:
        return self._config_parser.get(section, option)

    def get_options(self, section: str) -> List[str]:
        return self._config_parser.options(section)

import os
from configparser import ConfigParser
from typing import List

from ..tools.Singleton import Singleton

__all__ = ['ConfigHandler', '_BASE_DIR', "_CONFIG_HANDLER"]

_BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


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


_CONFIG_HANDLER = ConfigHandler(str(_BASE_DIR) + "/config.cfg")

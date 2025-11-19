# models/base.py
from abc import ABC, abstractmethod


class FlagGenerator(ABC):
    """所有 Flag 生成器的抽象基类"""

    def __init__(self, args):
        self.args = args

    @abstractmethod
    def generate(self) -> str:
        """生成一个 Flag 字符串"""
        pass

    @staticmethod
    @abstractmethod
    def add_arguments(parser):
        """为特定模型添加命令行参数"""
        pass
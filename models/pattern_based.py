# models/pattern_based.py
import string
import random
from .base import FlagGenerator


class PatternBasedGenerator(FlagGenerator):
    """根据指定模式生成 Flag"""

    def generate(self) -> str:
        pattern = self.args.pattern
        char_set = string.ascii_uppercase + string.digits

        def replace_char(c):
            if c == 'X':
                return random.choice(string.ascii_uppercase)
            elif c == 'Y':
                return random.choice(string.ascii_lowercase)
            elif c == 'Z':
                return random.choice(string.ascii_letters)
            elif c == '0':
                return random.choice(string.digits)
            elif c == '?':
                return random.choice(char_set)
            else:
                return c  # 非占位符字符保持不变

        return ''.join(map(replace_char, pattern))

    @staticmethod
    def add_arguments(parser):
        parser.add_argument(
            "--pattern",
            type=str,
            required=True,
            help="""生成 Flag 的模式。
                    X: 大写字母, Y: 小写字母, Z: 大小写字母,
                    0: 数字, ?: 字母或数字, 其他字符保持不变。
                    例如: "FLAG-XXXX-0000"."""
        )
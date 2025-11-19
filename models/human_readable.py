# models/human_readable.py
import string
import random
from .base import FlagGenerator


class HumanReadableGenerator(FlagGenerator):
    """生成人类可读的、有意义前缀的 Flag"""

    def generate(self) -> str:
        prefix = self.args.prefix
        separator = self.args.separator
        length = self.args.length

        char_set = string.ascii_uppercase + string.digits
        random_part = ''.join(random.choice(char_set) for _ in range(length))

        return f"{prefix}{separator}{random_part}"

    @staticmethod
    def add_arguments(parser):
        parser.add_argument(
            "--prefix",
            type=str,
            default="FLAG",
            help="Flag 的前缀 (默认: 'FLAG')"
        )
        parser.add_argument(
            "--separator",
            type=str,
            default="-",
            help="前缀和随机部分的分隔符 (默认: '-')"
        )
        parser.add_argument(
            "--length",
            type=int,
            default=12,
            help="随机部分的长度 (默认: 12)"
        )
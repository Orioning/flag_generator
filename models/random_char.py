# models/random_char.py
import string
import random
from .base import FlagGenerator


class RandomCharGenerator(FlagGenerator):
    """生成由随机字符组成的 Flag"""

    def generate(self) -> str:
        length = self.args.length
        char_set = string.ascii_letters + string.digits
        if self.args.special_chars:
            char_set += string.punctuation
        return ''.join(random.choice(char_set) for _ in range(length))

    @staticmethod
    def add_arguments(parser):
        parser.add_argument(
            "--length",
            type=int,
            default=16,
            help="生成的 Flag 长度 (默认: 16)"
        )
        parser.add_argument(
            "--special-chars",
            action="store_true",
            help="是否包含特殊字符 (默认: 不包含)"
        )
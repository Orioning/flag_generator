# models/hex_hash.py
import random
from .base import FlagGenerator


class HexHashGenerator(FlagGenerator):
    """生成类似哈希值的十六进制 Flag"""

    def generate(self) -> str:
        # 常见的哈希长度：MD5(32), SHA-1(40), SHA-256(64)
        lengths = {128: 32, 160: 40, 256: 64, 512: 128}

        if self.args.bits in lengths:
            length = lengths[self.args.bits]
        else:
            length = self.args.length

        return ''.join(random.choice('0123456789abcdef') for _ in range(length))

    @staticmethod
    def add_arguments(parser):
        parser.add_argument(
            "--bits",
            type=int,
            choices=[128, 160, 256, 512],
            help="模拟特定长度的哈希值 (128, 160, 256, 512 bits)，与 --length 互斥"
        )
        parser.add_argument(
            "--length",
            type=int,
            default=32,
            help="自定义十六进制字符串长度 (默认: 32)"
        )
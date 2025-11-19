# models/uuid.py
import uuid
from .base import FlagGenerator


class UUIDGenerator(FlagGenerator):
    """生成 UUID 格式的 Flag"""

    def generate(self) -> str:
        if self.args.version == 1:
            return str(uuid.uuid1())
        elif self.args.version == 3:
            # 需要一个命名空间和名称
            namespace = uuid.NAMESPACE_DNS
            name = f"example.com_{uuid.uuid4()}"
            return str(uuid.uuid3(namespace, name))
        elif self.args.version == 4:
            return str(uuid.uuid4())
        elif self.args.version == 5:
            namespace = uuid.NAMESPACE_DNS
            name = f"example.com_{uuid.uuid4()}"
            return str(uuid.uuid5(namespace, name))
        else:
            return str(uuid.uuid4())  # 默认

    @staticmethod
    def add_arguments(parser):
        parser.add_argument(
            "--version",
            type=int,
            choices=[1, 3, 4, 5],
            default=4,
            help="UUID 版本 (默认: 4)"
        )
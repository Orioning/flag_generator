# models/__init__.py
from .random_char import RandomCharGenerator
from .hex_hash import HexHashGenerator
from .uuid import UUIDGenerator
from .human_readable import HumanReadableGenerator
from .pattern_based import PatternBasedGenerator

# 模型注册表，键是命令行参数，值是对应的类
MODEL_REGISTRY = {
    "random": RandomCharGenerator,
    "hex": HexHashGenerator,
    "uuid": UUIDGenerator,
    "human": HumanReadableGenerator,
    "pattern": PatternBasedGenerator,
}

__all__ = [
    "MODEL_REGISTRY",
    "RandomCharGenerator",
    "HexHashGenerator",
    "UUIDGenerator",
    "HumanReadableGenerator",
    "PatternBasedGenerator",
]
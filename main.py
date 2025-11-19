#!/usr/bin/env python3
# main.py
import argparse
import sys
from models import MODEL_REGISTRY


def main():
    # 创建主解析器
    parser = argparse.ArgumentParser(
        description="一个功能强大的 Flag 生成器脚本",
        formatter_class=argparse.RawTextHelpFormatter
    )

    # 添加通用参数
    parser.add_argument(
        "-n", "--number",
        type=int,
        default=1,
        help="生成 Flag 的数量 (默认: 1)"
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        help="将结果输出到指定文件，而非控制台"
    )

    # 创建子解析器，用于不同的生成模型
    subparsers = parser.add_subparsers(
        dest="model",
        title="可用的生成模型",
        description="请选择一个生成模型，并查看其特定参数",
        required=True,
        help="生成模型的名称"
    )

    # 为每个模型添加子解析器
    for model_name, model_class in MODEL_REGISTRY.items():
        model_parser = subparsers.add_parser(model_name, help=f"{model_class.__doc__}")
        model_class.add_arguments(model_parser)

    # 解析参数
    args = parser.parse_args()

    # 初始化并生成 Flag
    try:
        generator_class = MODEL_REGISTRY[args.model]
        generator = generator_class(args)

        flags = [generator.generate() for _ in range(args.number)]

        # 输出结果
        if args.output:
            with open(args.output, 'w') as f:
                for flag in flags:
                    f.write(flag + '\n')
            print(f"成功生成 {args.number} 个 Flag，并保存到文件 '{args.output}'")
        else:
            print("生成的 Flag:")
            print("-" * 30)
            for i, flag in enumerate(flags, 1):
                print(f"{i}: {flag}")
            print("-" * 30)

    except Exception as e:
        print(f"发生错误: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
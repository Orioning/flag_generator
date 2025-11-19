Flag 生成器
一个功能强大、高度可扩展的 Python 脚本，用于生成各种类型和格式的 "Flag"。通过命令行参数，你可以轻松选择不同的生成模型、自定义生成规则，并将结果输出到控制台或文件中。
特性
多种生成模型：内置多种 Flag 生成算法，满足不同场景需求。
高度可配置：每个模型都支持丰富的参数自定义。
命令行友好：使用 argparse 提供清晰的参数说明和帮助信息。
模块化设计：采用插件式架构，方便你轻松添加新的生成模型。
灵活的输出：支持在控制台打印或保存到指定文件。

基本用法
直接运行 main.py 并通过 -h 或 --help 查看帮助信息。
bash
运行
# 查看整体帮助
python3 main.py -h

# 查看特定模型的帮助 (例如 'pattern' 模型)
python3 main.py pattern -h
生成模型详解
random - 随机字符组合
生成由大小写字母、数字（可选特殊字符）组成的随机字符串。
参数:
--length LENGTH: 生成的 Flag 长度 (默认: 16)。
--special-chars: 是否包含特殊字符 (默认：不包含)。
示例:
bash
运行
# 生成一个长度为 20 的随机字符串，包含特殊字符
python3 main.py random --length 20 --special-chars

# 生成 5 个长度为 10 的随机字母数字字符串
python3 main.py random -n 5 --length 10
hex - 十六进制哈希模拟
生成类似 MD5、SHA-1 等哈希值的十六进制字符串。
参数:
--bits {128,160,256,512}: 模拟特定长度的哈希值 (对应 MD5, SHA-1, SHA-256, SHA-512)。与 --length 互斥。
--length LENGTH: 自定义十六进制字符串的长度 (默认: 32)。
示例:
bash
运行
# 生成一个模拟 SHA-256 (64位) 的哈希值
python3 main.py hex --bits 256

# 生成一个长度为 10 的自定义十六进制字符串
python3 main.py hex --length 10
uuid - 通用唯一识别码
生成标准的 UUID 格式字符串。
参数:
--version {1,3,4,5}: 指定 UUID 版本 (默认: 4)。
1: 基于时间和 MAC 地址。
3: 基于命名空间的 MD5 哈希。
4: 完全随机。
5: 基于命名空间的 SHA-1 哈希。
示例:
bash
运行
# 生成一个 UUID v4
python3 main.py uuid

# 生成一个 UUID v1
python3 main.py uuid --version 1
human - 人类可读格式
生成带有前缀和分隔符的、易于阅读和识别的 Flag。
参数:
--prefix PREFIX: Flag 的前缀 (默认: 'FLAG')。
--separator SEPARATOR: 前缀和随机部分的分隔符 (默认: '-')。
--length LENGTH: 随机部分的长度 (默认: 12)。
示例:
bash
运行
# 生成一个默认格式的人类可读 Flag, 如 "FLAG-ABC123..."
python3 main.py human

# 生成一个自定义前缀和分隔符的 Flag, 如 "TOKEN_789XYZ..."
python3 main.py human --prefix "TOKEN" --separator "_" --length 8
pattern - 模式匹配
根据用户指定的模式生成 Flag，提供最高的灵活性。
参数:
--pattern PATTERN: (必需) 生成 Flag 的模式。
X: 代表一个随机大写字母。
Y: 代表一个随机小写字母。
Z: 代表一个随机大小写字母。
0: 代表一个随机数字。
?: 代表一个随机字母或数字。
其他任何字符：将作为固定字符保留。
示例:
bash
运行
# 生成一个符合 "COMPANY-XXXX-0000" 格式的 Flag
python3 main.py pattern --pattern "COMPANY-XXXX-0000"

# 生成一个复杂模式的 Flag, 如 "PROJ-?XYZ-###-2023"
python3 main.py pattern --pattern "PROJ-?XYZ-###-2023"
通用参数
这些参数可以在所有模型中使用：
-n NUMBER, --number NUMBER: 生成 Flag 的数量 (默认: 1)。
-o FILE, --output FILE: 将生成的所有 Flag 保存到指定文件中，每行一个。如果不指定，则打印到控制台。
示例:
bash
运行
# 生成 10 个 UUID 并保存到 uuid_list.txt 文件
python3 main.py uuid -n 10 -o uuid_list.txt

import ure as re

# 定义正则表达式模式
pattern = re.compile(r'\d+')

# 搜索字符串中的第一个匹配项
match = pattern.search('Hello 123 World')

# 如果找到了匹配项
if match:
    # 打印匹配到的内容
    print(match.group())
else:
    print('No match found')

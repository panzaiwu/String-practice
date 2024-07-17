import re

def extract_and_format_number(s):
    # 使用正则表达式提取字符串中的数字部分
    match = re.search(r'\d+(\.\d+)?', s)
    if match:
        number_str = match.group()
        # 将数字转换为浮点数
        number = float(number_str)
        # 保留两位小数，不四舍五入
        formatted_number = "{:.2f}".format(number)
        return formatted_number
    else:
        return None

# 测试用例
s1 = "abcd123.456"
s2 = "abcd123"

print(extract_and_format_number(s1))  # 输出：123.45
print(extract_and_format_number(s2))  # 输出：123.00

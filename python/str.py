"""
.replace(old, new, count=-1)
    replace()方法用于替换字符串中的指定子字符串。它接受三个参数：old表示要被替换的子字符串，new表示替换后的子字符串，count表示要替换的次数（默认为-1，表示替换所有匹配项）。
    replace()方法返回一个新的字符串，原字符串保持不变。
.split(sep=None, maxsplit=-1)
    split()方法用于将字符串分割成一个列表。它接受两个参数：sep表示分隔符，默认为None，表示以任意空白字符（空格、制表符、换行符等）作为分隔符；maxsplit表示最大分割次数，默认为-1，表示分割所有匹配项。
    split()方法返回一个列表，包含分割后的子字符串。
.strip([chars])
    strip()方法用于移除字符串两端的指定字符（默认为空格）。它接受一个可选参数chars，表示要移除的字符集合。如果省略该参数，strip()方法将移除字符串两端的空白字符。
    strip()方法返回一个新的字符串，原字符串保持不变。
"""

str1 = "Hello, World!"
# 使用replace()方法替换字符串中的子字符串
str2 = str1.replace("World", "Python")
print(str2)  # 输出: Hello, Python!
# 使用split()方法将字符串分割成一个列表
str3 = str1.split(", ")
print(str3)  # 输出: ['Hello', 'World!']
# 使用strip()方法移除字符串两端指定的字符
str4 = str1.strip("H!")
print(str4)  # 输出: ello, World

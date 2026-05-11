"""
.read(num): 读取num个字节的数据，返回一个字符串。
如果没有指定num或者num为负数，则读取并返回整个文件的内容。
.readline(): 读取一行数据，返回一个字符串。
.readlines(): 读取所有行数据，返回一个列表，每个元素是文件中的一行数据
在每一行的末尾包含换行符。
encoding='utf-8'：指定文件的编码格式为UTF-8，确保正确处理中文字符。
.close()：关闭文件，释放系统资源。
with open(...) as file: 这种方式会自动管理文件资源，
无论是否发生异常，都会确保文件被正确关闭。
.flush()：将缓冲区中的数据立即写入文件，确保数据的及时保存。
'w'：以写入模式打开文件，如果文件不存在则创建它，如果存在则清空其内容。
'a'：以追加模式打开文件，如果文件不存在则创建它，
如果存在则在文件末尾添加内容。
.seek(offset, whence)：移动文件指针到指定位置。
offset：偏移量，表示要移动的字节数。
whence：可选参数，表示偏移的参考位置，默认为0（文件开头）。
0：从文件开头开始计算偏移。
"""

file = open(r'python\test.txt', 'r', encoding='utf-8')
print(file.read())
file.seek(0)
print(file.read(10))
file.seek(0)
print(file.readline())
file.seek(0)
print(file.readlines())
file.close()
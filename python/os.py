"""
os.path.join('..', 'data')

"""

import os

print(os.getcwd())  # 获取当前工作目录
print(os.path.abspath('.'))  # 获取当前工作目录的绝对路径
print(os.path.abspath('..'))  
# 获取当前工作目录的父目录的绝对路径

# 在工作目录下创建一个新的文件夹
os.mkdir('data')
# os.mkdir()函数用于创建一个新的目录，
# 参数是要创建的目录的名称或路径。
# 如果目录已经存在，os.mkdir()会抛出FileExistsError异常。
os.makedirs('data')
# os.makedirs()函数用于递归创建目录，如果父目录不存在，
# 它会自动创建父目录。
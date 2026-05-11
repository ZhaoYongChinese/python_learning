"""
.keys() 取出字典的键，返回一个可迭代对象
.values() 取出字典的值，返回一个可迭代对象
.items() 取出字典的键值对，返回一个可迭代对象，每个元素是一个包含键和值的元组

"""

my_dict = {'a': 1, 'b': 2, 'c': 3}
# 获取键
keys = my_dict.keys()
print(keys,type(keys))  # 输出: dict_keys(['a', 'b', 'c'])
# 获取值
values = my_dict.values()
print(values,type(values))  # 输出: dict_values([1, 2, 3])
# 获取键值对
items = my_dict.items()
print(items,type(items))  # 输出: dict_items([('a', 1), ('b', 2), ('c', 3)])
"""
.sorted() 将一个可迭代对象进行排序，返回一个新的列表。
语法：
sorted(iterable, key=None, reverse=False)
参数说明：
iterable：要排序的可迭代对象。
key：一个函数，用来从每个元素中提取一个用于排序比较的键。默认为None，表示直接比较元素本身。
reverse：一个布尔值，表示是否反转排序结果。默认为False，表示按升序排序；如果设置为True，则按降序排序。
"""
my_list = [3, 1, 4, 1, 5, 9]
# 升序排序
sorted_list = sorted(my_list)
print(sorted_list)  # 输出: [1, 1, 3, 4, 5, 9]
# 降序排序 
sorted_list_desc = sorted(my_list, reverse=True)
print(sorted_list_desc)  # 输出: [9, 5, 4, 3, 1, 1]
# 使用 key 参数进行排序
my_list_of_tuples = [(1, 'b'), (2, 'a'), (3, 'c')]
sorted_by_second = sorted(my_list_of_tuples, key=lambda x: x[1])
print(sorted_by_second)  # 输出: [(2, 'a'), (1, 'b'), (3, 'c')]
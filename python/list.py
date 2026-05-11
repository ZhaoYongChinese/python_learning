"""
index()方法
"""
# index()方法返回列表中第一个匹配项的索引位置，如果没有找到匹配项，则会抛出ValueError异常。
show_list = [1, 2, 3, 4, 5, 5]
index_3 = show_list.index(3)
index_5 = show_list.index(5)
print(index_3, index_5)

# index()方法还可以接受一个可选的参数start，表示从列表的哪个位置开始搜索。默认值为0。
index_5_from_3 = show_list.index(5, 5)  # 从索引5开始搜索5
print(index_5_from_3)

# index()方法还可以接受一个可选的参数end，表示搜索的结束位置。默认值为列表的长度。
index_5_from_0_to_4 = show_list.index(5, 0, 5)  # 从索引0到索引4搜索5
print(index_5_from_0_to_4)

"""
append()方法
extend()方法
"""
# append()方法用于在列表末尾添加一个元素。
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)
# extend()方法用于在列表末尾一次性添加多个元素。
my_list.extend([5, 6])
print(my_list)
# append()方法和extend()方法的区别在于，append()方法将整个对象作为一个元素添加到列表中，而extend()方法将可迭代对象中的每个元素逐个添加到列表中。

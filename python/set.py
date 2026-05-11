"""
.differences(other)
    返回一个新的集合，包含在当前集合中但不在 other 集合中的元素。
.difference_update(other)
    从当前集合中移除在 other 集合中的元素。
.intersection(other)
    返回一个新的集合，包含在当前集合和 other 集合中都存在的元素
.intersection_update(other)
    从当前集合中保留在 other 集合中也存在的元素。
.union(other)
    返回一个新的集合，包含在当前集合和 other 集合中的所有元素。
"""

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
# 差集
diff = set1.difference(set2)
print(diff)  # 输出: {1, 2}
# 交集
inter = set1.intersection(set2)
print(inter)  # 输出: {3, 4}
# 并集
union = set1.union(set2)
print(union)  # 输出: {1, 2, 3, 4, 5, 6}
# 更新差集
set1.difference_update(set2)
print(set1)  # 输出: {1, 2}
# 更新交集
set1.intersection_update(set2)
print(set1)  # 输出: set()
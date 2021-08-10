# author: KaiZhang
# date: 2021/8/8 14:23

"""
如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。
在Python中，迭代是通过for ... in来完成的
"""

# dict迭代
"""
因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。
默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()。
"""

d = {'a': 1, 'b': 2, 'c': 3}  # 迭代key
for key in d:
    print(key)

for value in d.values():  # 迭代value
    print(value)

for key, value in d.items():
    print(key, "=", value)

# 当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。
# 那么，如何判断一个对象是可迭代对象呢？方法是通过collections.abc模块的Iterable类型判断：

from collections.abc import Iterable

print(isinstance('abc', Iterable))  # str是否可迭代 True

print(isinstance([1, 2, 3], Iterable))  # list是否可迭代 True

print(isinstance(123, Iterable))  # 整数是否可迭代 False

# 如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i, value in enumerate(['A', 'B', 'C']):
    print(i, "=", value)

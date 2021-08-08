"""
author: KaiZhang
date: 2021/8/7 16:17
"""

"""
dict
字典是另一种可变容器模型，且可存储任意类型对象。
字典的每个键值 key=>value 对用冒号 : 分割，每个键值对之间用逗号 , 分割，整个字典包括在花括号 {} 中
"""
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

# 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入：
d['Adam'] = 67
print(d)

# 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉
d['Jack'] = 90
print(d)
d['Jack'] = 88
print(d)

# 如果key不存在，dict就会报错
# print(d['kayaking'])

"""
要避免key不存在的错误，有两种办法
一是通过in判断key是否存在
二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
"""
print('Thomas' in d)
result1 = d.get('Thomas')
print(result1)

result2 = d.get('Thomas', -1)
print(result2)  # 没有获取到，返回-1

# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除
pop = d.pop('Bob')
print(d)
print(pop)

# 删除字典元素，能删单一的元素也能清空字典，清空只需一项操作。显示删除一个字典用del命令，如下实例：
del d['Michael']  # 删除键是'Michael'的条目
print(d)

# 清除字典所有条目
d.clear()
print(d)

# 删除字典
# del d
# print(d) # 字典删除后，再使用时会报字典不存在

"""
list、dict
dict特点
1、查找和插入的速度极快，不会随着key的增加而变慢；
2、需要占用大量的内存，内存浪费多。

list特点
1、查找和插入的时间随着元素的增加而增加；
2、占用空间小，浪费内存很少。
所以dict是用空间来换取时间的一种方法

注意：
dict的key必须是不可变对象。
这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。
要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key
"""
key = [1, 2, 3]
# d[key] = 'a list'  # 报错

# author: KaiZhang
# date: 2021/8/3 23:53

"""
列表特点：
1、列表元素按顺序有序排序
2、索引映射唯一数据
3、列表可以存储重复数据
4、任意数据类型混存
5、根据需要动态分配和回收内存
"""

# list创建的两种方式

# 第一种方式，使用"[]"
list1 = ['张三', '李四', 12, True]
print(id(list1))
print(type(list1))
print(list1)

# 第二种方式，使用内置函数list()

list2 = list(['哈哈哈', '呵呵呵', '嘻嘻嘻', '呵呵呵'])
print(id(list2))
print(type(list2))
print(list2)
print(list2[0])
print(list2[-3])  # 逆序取值[-0]与[0]相同都是取第一个，从[-1]开始取倒数第一个

# list.index
"""
list.index(x[, start[, end]])
函数用于从列表中找出某个值第一个匹配项的索引位置
x：查找的对象。
start： 可选，查找的起始位置。
end：可选，查找的结束位置。
返回值：该方法返回查找对象的索引位置，如果没有找到对象则抛出异常。
"""
print(list2.index('嘻嘻嘻', 2, 10))
print(list2.index('呵呵呵'))  # 取出列表中'呵呵呵'的索引，如果有多个相同的，则取第一个。如果取得值（比如’啦啦‘）不在列表中，则抛出异常'啦啦' is not in list

# 对列表进行操作
list3 = ['Michael', 'Bob', 'Tracy']
# 往list中追加元素到末尾
list3.append('append')
print(list3)
# 把元素插入到指定位置x
list3.insert(1, 'insert')
print(list3)

"""
pop 删除并返回索引处的项目（默认最后）。如果列表为空或索引超出范围，则引发 IndexError。
"""
# 删除list末尾的元素
pop = list3.pop()
print(list3)
print(pop)
# 删除指定位置的元素，用pop(i)方法，其中i是索引位置
popList = list3.pop(1)  #
print(list3)
print(popList)

# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
list3[0] = 'replace'
print(list3)

# list中的元素类型可以不同
list4 = ['a', 1, True]
print(list4)

# list元素也可以是另一个list
list5 = ['python', 'java', ['asp', 'php'], 'scheme']
print(list5)
print(len(list5))
print(list5[2][1])  # 获取其中的php，相当于二维数组


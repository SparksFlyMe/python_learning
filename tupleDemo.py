# author: KaiZhang
# date: 2021/8/7 16:00

"""
tuple
元组与列表类似，不同之处在于元组的元素不能修改
元组使用小括号，列表使用方括号
不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple
"""

# tup1不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用tup1[0]，tup1[-1]，但不能赋值成另外的元素。
tup1 = ('Michael', 'Bob', 'Tracy')

# tuple的一个陷阱，只有1个元素的tuple定义时必须加一个逗号“,” 因为如果不加逗号比如tup=(1)，则会被认为定义了1这个数
tup2 = (1,)
tup3 = (1)
print(type(tup2))
print(type(tup3))

# 看一个“可变的”tuple
t = ('a', 'b', ['A', 'B'])
print(t)
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
# 表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。tuple一开始指向的list并没有改成别的list，
# 所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！

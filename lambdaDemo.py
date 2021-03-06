# author: KaiZhang
# date: 2021/8/8 16:46

"""
lambda :匿名函数
当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便
"""
l = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(l)

"""
通过对比可以看出，匿名函数lambda x: x * x实际上就是：
def f(x):
    return x * x
    
关键字lambda表示匿名函数，冒号前面的x表示函数参数。
匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。    
"""


# 同样，也可以把匿名函数作为返回值返回
def build(x, y):
    return lambda: x * x + y * y

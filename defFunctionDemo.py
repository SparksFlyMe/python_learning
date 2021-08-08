# author: KaiZhang
# date: 2021/8/8 10:07

"""
在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回
"""
import math


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


result = my_abs(-99)
print(result)
"""
请注意，函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑。
如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。return None可以简写为return
"""


# 函数返回多个值
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
"""
结果151.96152422706632 70.0，看似返回两个值， 但其实这只是一种假象，Python函数返回的仍然是单一值，原来返回值是一个tuple！但是，在语法上，返回一个tuple
可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
"""


# 设置位置参数、默认参数
def enroll(name, gender):  # name、gender位置参数
    print('name:', name, 'gender:', gender)


enroll("张三", 8)
enroll(name="赵武", gender=10)


# 函数新增age、city两个参数
def enroll(name, gender, age=6, city='Beijing'):  # age、city是默认参数
    print('name:', name, 'gender:', gender, 'age:', age, 'city:', city)


enroll("李四", 9)  # 如果函数定义不给age、city默认值即def enroll(name, gender, age, city):，则再调用原来两个参数的方法会报错

enroll("王五", 8, city="shanghai", age=20)  # 可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上


# 定义默认参数要牢记一点：默认参数必须指向不变对象
def add_end(L=[]):  # L=[]是默认可变参数
    L.append('END')
    return L


print(add_end([1, 2, 3]))  # 结果为：[1, 2, 3, 'END']。 给了[1, 2, 3]列表，所以不用默认参数

print(add_end())  # 结果为['END']。 没有给参数，所以用默认参数
print(add_end())  # 结果为['END', 'END']。因为没有给参数，所以用默认参数，但此时L已经是['END']了
print(add_end())
"""
Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
"""


# 要修改上面的例子，我们可以用None这个不变对象来实现
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end())  # 结果为['END']。无论调用多少次，都不会有问题
print(add_end())  # 结果为['END']。无论调用多少次，都不会有问题
print(add_end())  # 结果为['END']。无论调用多少次，都不会有问题
print(add_end())  # 结果为['END']。无论调用多少次，都不会有问题
"""
为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。此外，由于对象不变，
多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象
"""

# 可变参数
"""
def functionName([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]
加了星号（*）的变量名会存放所有未命名的变量参数
"""


def calc(*numbers):  # 在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2, 3))

# 如果已经有一个list或者tuple，要调用一个可变参数怎么办
# 方法一
nums = [1, 2, 3]
print(calc(nums[0], nums[1], nums[2]))
# 方法二 Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
print(calc(*nums))  # *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。

# 关键字参数
"""
可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
关键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数，但是，如果调用者愿意提供更多的参数，我们也能收到。
试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。
"""


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')


# 命名关键字参数
# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查


def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)


person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)


# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下
def person(name, age, *, city, job):
    print(name, age, city, job)


# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
person('Jack', 24, city='Beijing', job='Engineer')
person('Jack', 24, city='Beijing', job='Engineer')

# 参数组合
"""
在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
"""


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f2(1, 2, d=99, ext=None)

"""
默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
要注意定义可变参数和关键字参数的语法：
*args是可变参数，args接收的是一个tuple；
**kw是关键字参数，kw接收的是一个dict。
以及调用函数时如何传入可变参数和关键字参数的语法：
可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
"""

# author: KaiZhang
# date: 2021/8/8 16:22

"""
高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

"""


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum  # 不返回求和的结果，而是返回求和的函数


f = lazy_sum(1, 3, 5, 7, 9)
print(type(f), f)
print(f())  # 调用函数f()时，才真正计算求和的结果

"""
一个函数可以返回一个计算结果，也可以返回一个函数。
返回函数不要引用任何循环变量，或者后续会发生变化的变量
!!!返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。
"""

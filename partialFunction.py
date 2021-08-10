# author: KaiZhang
# date: 2021/8/9 23:16

"""
偏函数
把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
"""

import functools

int2Func = functools.partial(int, base=16)
print(int2Func('12345'))

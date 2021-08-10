# author: KaiZhang
# date: 2021/8/8 15:46

"""
filter()函数用于过滤序列。
和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
"""


# 在一个list中，删掉偶数，只保留奇数，可以这么写
def is_odd(n):
    if n % 2 == 0:
        return True
    else:
        return False


f = filter(is_odd, [1, 2, 3, 4, 5, 6])
print(type(f), list(f))

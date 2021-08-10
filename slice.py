# author: KaiZhang
# date: 2021/8/8 14:07

"""
切片
"""
L = list(range(100))
print(L)

print(L[:10])  # 前十个数

print(L[-10:])  # 后是个数

print(L[10:20])  # 前11-20个数

print(L[:10:2])  # 前10个数，每两个取一个

print(L[::5])  # 所有数，每5个取一个

print(L[:])  # 什么都不写，只写[:]就可以原样复制一个list

# author: KaiZhang
# date: 2021/8/2 21:44

# 创建一个整数列表
"""
range(start, stop[, step])
参数说明：

start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
"""

r1 = range(5)
print(list(r1))

r2 = range(1, 10)
print(list(r2))

r3 = range(2, 10, 3)
print(list(r3))
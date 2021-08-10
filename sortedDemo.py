# author: KaiZhang
# date: 2021/8/8 15:51

"""
排序算法
排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。如果是数字，我们可以直接比较，但如果是字符串或者两个dict呢？直接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数抽象出来。
Python内置的sorted()函数就可以对list进行排序
"""

s = sorted([36, 5, -12, 9, -21])  # 默认正序排序
print(type(s), s)

s1 = sorted([36, 5, -12, 9, -21], reverse=True)  # 逆序排序
print(type(s1), s1)

# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序
s2 = sorted([36, 5, -12, 9, -21], key=abs)
print(type(s2), s2)

# 按首字母字符串顺序排序
s3 = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(type(s3), s3)

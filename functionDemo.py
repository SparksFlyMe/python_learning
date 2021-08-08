# author: KaiZhang
# date: 2021/8/8 10:02

"""
Python内置了很多有用的函数，我们可以直接调用
通过help(abs)查看abs函数的帮助信息
"""
help(abs)

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
a = abs  # 变量a指向abs函数
value = a(-1)
print(value)

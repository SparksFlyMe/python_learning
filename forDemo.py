# author: KaiZhang
# date: 2021/8/3 22:16

for letter in 'Python':  # 第一个实例
    print("当前字母: %s" % letter)
pass

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:  # 第二个实例
    print('当前水果: %s' % fruit)
pass

# 通过序列索引迭代
fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print('当前水果 : %s' % fruits[index])
pass

# 循环使用 else 语句
"""for … else 表示这样的意思，for 中的语句和普通的没有区别，else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行，while … else 也是一样。"""
for i in range(5):
    if i > 3:
        print(i)
else:
    print('hello world')  # for循环正常执行完了，所以会打印

for i in range(5):
    if i > 3:
        print(i)
        break
else:
    print('hello world')  # for循环被提前终止了，所以不会打印hello world
pass

# 如果在循环中不需要使用到自定义变量，可将自定义变量写为“_”下划线
for _ in range(5):
    print("haha")

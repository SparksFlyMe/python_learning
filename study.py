# author: KaiZhang
# date: 2021/8/1 11:02

# 引入decimal包
from decimal import Decimal

# 浮点数计算结果不精确，用decimal计算
print("===============================decimal================")
print(1.1 + 2.2)
print(Decimal("1.1") + Decimal("2.2"))
print("===============================decimal================")

# 获取变量的id（内存地址）、变量类型
print("=========================获取变量id、类型===============")
t = 2.222
print("类型", type(t))
print("id", id(t))
print("=========================获取变量id、类型===============")

# 字符串中，三个引号（三个单引号或者三个单引号）中内容可以换行展示
print("=========================三个引号换行===================")
print("""我可以换行，这是第一行
这是第二行,
这是第三行""")
print("=========================三个引号换行===================")

# 类型转换，不同类型变量之间的转换
name = "张三"
age = 20
height = "1.88"
print("转换前age属性", type(age), "转换后age属性", type(str(age)))
print("转换前height属性", type(height), "转换后height属性", type(float(height)))

# if else
judgmentA = 10
judgmentB = 10

# 普通判断
if judgmentA > judgmentB:
    print(str(judgmentA) + "大于" + str(judgmentB))
else:
    print(str(judgmentA) + "小于" + str(judgmentB))
# if、else if多分支判断
if judgmentA > judgmentB:
    print(str(judgmentA) + "大于" + str(judgmentB))
elif judgmentA == judgmentB:
    print(str(judgmentA) + "等于" + str(judgmentB))
else:
    print(str(judgmentA) + "小于" + str(judgmentB))

# 条件表达式，如果表达式结果为 true 则执行表达式左边部分，如果为 false 则执行表达式右边部分
print(str(judgmentA) + "大于" + str(judgmentB) if judgmentA > judgmentB else str(judgmentA) + "小于" + str(judgmentB))

# pass 是空语句，是为了保持程序结构的完整性。 pass 不做任何事情，一般用做占位语句。
passA = 10
passB = 20
if passA > passB:
    pass
else:
    pass

# in、not in
# in	如果在指定的序列中找到值返回 True，否则返回 False。	x 在 y 序列中 , 如果 x 在 y 序列中返回 True。
# not in	如果在指定的序列中没有找到值返回 True，否则返回 False。	x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。
inStrA = "abide"
inStrB = "i"
print(inStrB in inStrA)  # 返回true
print(inStrB not in inStrA)  # 返回false

# is、is not
# is 是判断两个标识符是不是引用自一个对象	x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
# is not 是判断两个标识符是不是引用自不同对象	x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。
isA = 20
isB = 20

if isA is isB:
    print("1 - a 和 b 有相同的标识")
else:
    print("1 - a 和 b 没有相同的标识")

if isA is not isB:
    print("2 - a 和 b 没有相同的标识")
else:
    print("2 - a 和 b 有相同的标识")


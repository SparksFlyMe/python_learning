# author: KaiZhang
# date: 2021/8/3 21:57

a = 1
while a < 10:
    print(a)
    a += 1

b = 0
sum1 = 0
while b <= 4:
    sum1 += b
    b = b + 1
print(sum1)

# while else 用键盘输入三次数，如果有一次等于888则退出不打印"对不起，三次密码均输入次数"，否则打印
c = 0
while c < 3:
    pwd = input('请输入密码：')
    if pwd == "888":
        print("密码输入正确")
        break
    else:
        print("密码输入错误")
    c += 1
else:
    print("对不起，三次密码均输入次数")

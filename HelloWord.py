print("hello world")
print("中文是否乱码")

# 输出hello word 到文件a.txt中
fp = open('C:/Users/kaizhang/Desktop/a.txt', 'a+')
print("hello word", file=fp)

fp.close()

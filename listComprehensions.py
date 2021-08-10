# author: KaiZhang
# date: 2021/8/8 14:44
"""
List Comprehensions ：列表生成式
"""
range_ = [x * x for x in range(1, 11)]
print(range_)

x_ = [x for x in range(1, 11) if x % 2 == 0]  # 不能在最后的if加上else，因为跟在for后面的if是一个筛选条件，不能带else，否则无法筛选

x_ = [x if x % 2 == 0 else -x for x in range(1, 11)]  # if写在for前面必须加else，因为for前面的部分是一个表达式，它必须根据x计算出一个结果。因此，考察表达式：x if x  % 2 == 0，它无法根据x计算出结果，因为缺少else，必须加上else

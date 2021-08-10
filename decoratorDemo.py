# author: KaiZhang
# date: 2021/8/8 17:02

"""
装饰器
"""


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log("execute")
def now():
    print("2021-08-08")


now()  # 等于执行了now = log('execute')(now)




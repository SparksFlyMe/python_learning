# author: KaiZhang
# date: 2021/8/11 22:20

"""
定义一个类。class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的。
通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
"""


class Student(object):
    pass


stu = Student()  # 创建一个student实例 类名+()


class Student(object):
    def __init__(self, name, score):  # 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
        # 定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：
        self.name = name
        self.score = score


student = Student("张三", 85)

print(student.name, student.score)
"""
注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去
和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。
"""


# 数据封装
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


s1 = Student("王五", 99)
s1.print_score()
print(s1.name)

# 访问限制
"""
如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问，所以，我们把Student类改一改
"""


class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))


s2 = Student("六六", 50)


# s2.__name  # 报错：'Student' object has no attribute '__name'，因为__name已经是私有变量了

# 但是如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):  # get方法
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, name):  # set方法
        self.__name = name

    def set_score(self, score):
        self.__score = score

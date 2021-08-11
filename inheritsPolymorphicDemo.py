# author: KaiZhang
# date: 2021/8/11 23:12

"""
继承和多态
"""


class Animal(object):
    def run(self):
        print("动物会跑")


class Dog(Animal):
    pass


dog = Dog()
dog.run()

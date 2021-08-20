# -*- coding:utf-8 -*-
# @Time: 2021/8/18 3:15 下午
# @Author: Elvin
'''单例模式'''
class Func:
    def __init__(self, age, name):
        self.age = age
        self.name = name

func = Func() #func也成为Foo类的实例
func1 = Func()

#单例模式用于同一份实例

class Foo:

    __v = None

    @classmethod
    def get_instance(cls):
        if cls.__v:
            return cls.__v
        else:
            cls.__v = Foo()
            return cls.__v
obj1 = Foo.get_instance()
print(obj1)
obj2 = Foo.get_instance()
print(obj2)
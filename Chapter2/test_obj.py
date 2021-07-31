# -*- coding:utf-8 -*-
# @Time: 2021/7/29 6:55 下午
# @Author: Elvin
'''
1.类变量（属性）：类变量在整个实例化的对象中是公用的。类变量定义在类中，且在方法之外。类变量通常不
作为实例变量使用。类变量也称作属性。
2.数据成员：类变量或实例变量用于处理类及其实例对象的相关数据。
3.方法重写：如果从父类继承的方法不能满足子类的需求，就可以对其进行改写，这个过程称为方法的覆盖。
4.实例变量：定义在方法中的变量只作用于当前实例的类。
5.多态：对不同类的对象使用同样的操作。
6.封装：对外部隐藏工作细节。
7.继承：即一个派生类继承基类的字段和方法。继承允许把一个派生类的对象作为一个基类对象对待，以普通类为基础建立专门的类对象。
'''
#方法的调用需要绑定到特定的对象上，函数不需要绑定。
class MyClass(object):
    i = 123
    def f(self):
        return 'hello world'

use_class = MyClass()
print(f'调用类的属性：{use_class.i}')
print(f'调用类的方法：{use_class.f()}')

#一个类中可定义多个构造方法，但实例化类时只实例化最后的构造方法
#获取私有属性值
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def info(self):
        print(f'学生：{self.name}; 分数：{self.__score}')

    def get_score(self):
        return self.__score

stu = Student('xiaowang',70)
print(f'修改分数：{stu.get_score()}')
stu.info()
print(f'修改后分数：{stu.get_score()}')

#设置私有属性值
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def info(self):
        print(f'学生：{self.__name}; 分数：{self.__score}')

    def set_score(self, score):
        self.__score = score

stu = Student('xiaomming', 97)
print(f'修改前分数：{stu.get_score()}')
stu.info()
stu.set_score(20)
print(f'修改后分数：{stu.get_score()}')
stu.info()

#私有方法self.__private_methods
class PrivateMethod(object):
    def __init__(self):
        pass

    def __foo(self):
        print('这是私有方法')

    def foo(self):
        print('公共方法')
        print('公共方法中调用私有方法')
        self.__foo()
        print('方法调用结束')

pri_pub = PrivateMethod()
print('开始调用公共方法：')
pri_pub()
print('开始调用私有方法')
pri_pub.__foo()

'''继承'''

class Person(object):
    def __init__(self,age):
        self.__age = age

    def age(self): #通过这层包装，继承的子类通过访问此方法来访问私有属性
        return self.__age

    def __set_age(self,age): #这是私有方法，子类也无法直接访问。
        self.__age = age     #但Person类可以访问内部的私有方法

    def setAge(self,age):    #子类的实例可以正常调用此方法
        self.__set_age(age)

class Student(Person):
    def dis(self):
        print(self.age())

if __name__ == "__main__":
    stu = Student(12)
    stu.dis()
    stu.setAge(22)
    stu.dis()

'''类方法'''
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

stu = Student('名字',10)

def info(): #普通方法的调用
    print(f'学生：{stu.name}; 分数：{stu.score}')
info(stu)


class Student0(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def info(self): #类方法
        pass
        print(f'学生：{self.name}；分数: {self.score}')

stu = Student('小明', 12)
stu.info()


class Dog:
    name = "老王"
    def __init__(self):
        self.name = "老张"

    def test_01(self):
        print("类内部访问name属性id=",id(self.name))
        print("类内部访问name属性=",self.name) #类内部访问name属性

if __name__ == '__main__':
    cl = Dog()
    cl.test_01() #调用test_01方法，在类内部对实例属性进行访问
    print("类外部访问name属性id=",id(cl.name))
    print("类外部访问name属性=",cl.name)
# 输出：
# 类内部访问name属性id= 4388310512
# 类内部访问name属性= 老网
# 类外部访问name属性id= 4388310512
# 类外部访问name属性= 老网

'''多重继承'''

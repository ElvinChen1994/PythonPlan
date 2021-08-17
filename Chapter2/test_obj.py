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
class Animal(object):
    pass


class Bird(Animal):
    pass


class Fly(object):
    pass


class Parrot(Bird,Fly):
    pass


class A(object):
    def m(self):
        print("m of A ")

#
# class B(A):
#     pass
#
#
# class C(A):
#     def m(self):
#         print("m of C ")
#
#
# class D(B, C): #使用广度优先，从左到右的原则寻找属性和方法
#     pass
# a = A()


class F:

    def f1(self):
        print('F.f1')

    def b2(self):
        print('F.f2')


class C(F):
    def c1(self):
        print('C.c1')

    def c2(self):
        print('C.c2')

obj = C()
obj.c1() #c1中的self是形参，指obj
obj.b2() #self用于指调用方法的调用者

class F:

    def f1(self):
        print('F.f1')

    def c2(self):
        print('F.f2')


class C(F):
    def c1(self):
        print('C.c1')

    def c2(self):
        print('C.c2')
        #super(C, self).c2()#执行父类中的方法，
        F.f1(self)#另一种调用父类的方法，self需要收到传入

obj = C()
obj.c1() #c1中的self是形参，指obj
obj.b2() #self用于指调用方法的调用者


class BaseOne():

    pass


class EveryOne(BaseOne):

    def sever_one(self):
        self.pro_one()  #调用的顺序是按照子类中的从左向右去查找

    def pro_one(self):
        print('this pro')


class EveryTwo:

    def pro_one(self):
        print('this pro two')


class EveryThree(EveryTwo,EveryOne):
    pass

obj = EveryThree()
obj.sever_one()


class BaseOne():

    def __init__(self):
        print('this is base one')



class EveryOne(BaseOne):

    def __init__(self): # 若出现两个初始化方法，只执行一个
        print('this is zero')
        BaseOne.__init__(self) #若想父类的初始化方法也执行，需要进行调用

    def sever_one(self):
        self.pro_one()

    def pro_one(self):
        print('this pro')


class EveryTwo:

    def pro_one(self):
        print('this pro two')


class EveryThree(EveryTwo,EveryOne):
    pass

obj = EveryThree()


class Feel:
    #静态字段，属于类，执行可以通过对象访问，也可以通过类访问
    age = 10

    def __init__(self, name):
        #普通字段，属于对象,只能通过对象访问
        self.name = name

    #普通方法
    def show(self):
        print(self.name)

    @staticmethod  #静态方法，此时self,可以不传，直接通过类调用
    def stat():
        print('123')

    @property #属性，用于获取值
    def per(self):
        print('232')

    @per.setter #设置值
    def per(self,svr):
        print(svr)

obj = Feel('wangwang')
obj.name
obj.show()
Feel.age
Feel.show(obj) #类方法，需要传入对象
Feel.stat()
obj.per #调用方法，已字段的方式访问


class Foo:

    def foo(self):
        return 333

    por = property(fget=foo)

    # @property   与上面实现一致
    # def por(self):
    #     return 333

obj = Foo()
res = obj.por
print(res)

'''成员修饰符：公有成员、私有成员   '''
class Foo:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def show(self):
        return Foo.__age

foo = Foo()
print(foo.__age)#私有属性无法通过外部访问，
res = foo.show()
print(res)


class Foo:

    def __f2(self): #私有方法
        return 123

    def f3(self):
        r = self.__f2()#通过对象调用私有方法
        return r

obj = Foo()
ret = obj.__f1()
print(ret)


class Feel:
    def __init__(self):
        self.__gen = 123
        self.ge = 44


class FeelGood(Feel):
    def __init__(self, name):
        self.name = 123
        super(FeelGood, self).__init__()

    def show(self):
        print(self.ge)  # 子类只能访问父类的公有字段


s = FeelGood()

class Foo:
    def __init__(self):
        print('初始方法')

    def __call__(self, *args, **kwargs):
        print('call')

obj = Foo()
obj() #该调用方式与__call__方法使用
Foo()()#与obj()一致

#使用isinstance()函数
#isinstance(a,A)

'''多态：python原生就是多态，有多种类型，其他语言明确指定某种类型'''

'''__len__方法'''
class Two:
    def __init__(self, N):
        self.N = N
        self.even_list = [2 * x for x in range(N)]

    def __len__(self):
        return self.N

two = Two(10)
print(len(two))

'''__str__'''
class Foo:
    def __init__(self, m, a):
        self.name = m
        self.age = a

    def __str__(self):
        return '%s-%s' %(self.name, self.age)


obj = Foo('xiaohyang', 13)
print(obj) #print(str(obj))
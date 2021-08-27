# -*- coding:utf-8 -*-
# @Time: 2021/7/27 8:49 上午
# @Author: Elvin
'''计算平均分配'''
m = int(input('m= '))
n = int(input('n= '))
fm = 1
for num in range(1, m + 1):
    fm *= num
fn = 1
for num in range(1, n + 1):
    fn *= num
fm_n = 1
for num in range(1,m - n + 1):
    fm_n *= num
print(fm // fn //fm_n)

'''阶乘'''
def fac(num):
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result
m = int(input('m = '))
n = int(input('n = '))
print(fac(m) // fac(n) // fac(m - n))

'''参数传递'''
from random import randint

def roll_dice(n=2):
    total = 0
    for _ in range(n):
        total += randint(1,6)
    return total

def add(a=0, b=0, c=0):
    return a + b + c

print(roll_dice())
print(roll_dice(3))
print(add())
print(add(1))
print(add(1,2))
print(add(1,2,3))
print(add(c=10, a=20, b=30))

'''可变参数'''
def add(*args):
    total = 0
    for val in args:
        total += val
    return total
print(add())
print(add(1))
print(add(1,3,5,7))

'''相同函数，后面的函数会覆盖之前的函数'''
def foo():
    print("this is one")

def foo():
    print("this is two")

foo()

'''通过导入模块的方式避免包的重复'''
#from module1 import foo#

# 输出hello, world!
foo()

#from module2 import foo

# 输出goodbye, world!
foo()

'''实现最大公约数和最小公倍数'''
def gcd(x,y):
    (x, y) = (y, x) if x > y else (x,y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor

def lcm(x, y):
    return x * y // gcd(x, y)

print(gcd(9, 18))
print(lcm(9,18))

'''回文数'''
def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num
print(is_palindrome(112))

'''第二种方法'''
Num = input('please input a number:')
if Num[:] == Num[::-1]:
    print('True')
else:
    print('False')

def foo():
    #global a
    #a=200
    a = 100
    print(a)  # 200


if __name__ == '__main__':
    nonlocal a

    foo()
    print(a)  # 100

'''nonlocal声明的变量不是局部变量,也不是全局变量,而是外部嵌套函数内的变量'''

def nonlocal_test():
    count = 0

    def test2():
        nonlocal count
        count += 1
        return count

    return test2

val = nonlocal_test()
print(val())
print(val())
print(val())

''':return'''
#返回值和无返回值，没有返回值默认返回一个None;有返回值，可以返回return,但是需要加上具体值
#无返回值
def no_return():
    print('no return 函数不写return语句')

def just_return():
    print('函数只写return，不返回具体内容')

def return_val():
    x=10
    y=10
    z = x + y
    print('函数返回具体结果')
    return z
return_val()

'''函数返回函数'''
def sum_late(*args):
    def calc_sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return calc_sum()
print(sum_late(5))
calc_sum = sum_late(1,2)
print(calc_sum)
'''闭包：如果在一个函数内部中对外部函数（不在全局作用域）的变量进行引用，内部函数称为闭包'''
def func_count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = func_count()
print(f'f1的结果是：',{f1()})
#返回闭包时，返回函数不要引用任何循环变量或后续会发生变化的变量，否则很容易出现你意想不到的问题。

'''递归函数：一个函数内部调用自身'''

def recurision():
    return recurision()  #无穷递归，理论上永远不会结束

#可用的递归：当函数直接返回值时有基本实例，递归实例，包括一个或多个问题最小部分的递归调用。
def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)
#递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的。每当进入一个函数调用，栈就会加一层栈帧；每当函数返回，栈就会减一层栈帧。
'''lambda'''
#lambda函数拥有自己的命名空间，不能访问自有参数列表之外或全局命名空间的参数
lambda x,y: x + y
#使用匿名函数：程序一次性使用、不需要定义函数名时，用匿名函数可以节省内存中定义变量所占的空间；如果想让程序更加简洁，使用匿名函数就可以做到。
#规则：一行表达式，必须有返回值；不能有return；可以没有参数，也可以有一个或多个参数。

t = lambda x,y : x * y
t(2,3) #匿名函数调用
t1 = lambda x, y=3: x + y
t1(2) #使用默认值

'''偏函数'''
#通过functools模块被调用，偏函数是将所要承载的函数作为partial()函数的第一个参数，原函数的各个参数依次作为partial()函数的后续参数，除非使用关键参数。

'''装饰器'''
#函数对象可以赋值给变量，通过变量调用该函数;不修改原来的函数，为改函数增加功能
def fuc():
    print('函数名称是：')
f = fuc
f()
print(fuc.__name__)

def log(func):
    def wrapper(*args,**kwargs):
        print('call %s()'% func.__name__)
        return func(args,**kwargs)
    return wrapper()

'''列表生成式'''
#for前面的if..else是表达式，for后面的if是过滤条件，不能加else
[x if x % 2 == 0 else -x for x in range(1, 11)]

x = 123
print(isinstance(x, int))#判断变量是不是整型

'''zip()迭代'''
li = ['a', 'b', 'c', 'd', 'e']
for i,e in zip(range(len(li)),li):
    print("index:",i,"element:",e)

'''使用enimerate迭代序列'''
li = ['a', 'b', 'c', 'd', 'e']

for i,e in enumerate(li):
    print("index:",i,"element:",e)
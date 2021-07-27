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
# -*- coding:utf-8 -*-
# @Time: 2021/7/26 3:34 下午
# @Author: Elvin
'''水仙花数'''
for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)

'''正整数反转'''
num = int(input("num = "))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)

'''穷举法'''
for x in  range(0,10):
    for y in range(0, 20):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公鸡：%d, 母鸡：%d, 小鸡：%d' % (x, y, z))

'''斐波那契'''
def fib(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a
print(fib(10))

'''*************'''
def fib1(n): #使用递归
    if n == 1 or n == 2:
        return 1
    return fib1(n-1) + fib1(n-2)
print(fib1(10))

'''***************'''

def fib3(n):  #输出指定的序列
    if n == 1:
        return [1]
    if n == 2:
        return [1,1]
    fibs = [1,1]
    for i in range(2,n):
        fibs.append(fibs[-1]+fibs[-2])
    return fibs

print(fib3(10))

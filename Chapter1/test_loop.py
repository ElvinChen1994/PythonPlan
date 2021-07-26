# -*- coding:utf-8 -*-
# @Time: 2021/7/26 12:26 下午
# @Author: Elvin

'''for in '''
sum = 0
for x in range(100):
    sum += x
print(sum)

'''增加歩长'''
sum = 0
for x in range(1,100,2):
    sum += x
print(sum)

'''while 循环'''
import random

answer = random.randint(1,100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入：'))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('答对了')
        break
print('你猜对的次数%d次'%counter)

'''循环嵌套'''
for i in range(1,10):
    for n in range(1, i+1):
        print('%d*%d=%d'%(i,n+1,i*n),end='\t')
    print()

'''判断一个整数是不是素数'''
from math import sqrt  #需要平方根的值

num = int(input('请输入一个正整数：'))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数'% num)
else:
    print('%d不是素数'% num)
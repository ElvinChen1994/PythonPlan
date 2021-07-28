# -*- coding:utf-8 -*-
# @Time: 2021/7/28 1:57 下午
# @Author: Elvin
# '''字符串转义\\'''
a1 = '\'hello\''
print(a1)
a2= '\n\hello\\\n' # \n代表换行 \t 表示制表符
print(a2)
a3 = '\thello\t'
print(a3)

t1= '\141\142\143\x61' #\后面可以跟一个八进制和十六进制的表示字符，\141代表小写字母a,后面x61是十六进制表示法
t2 = '\u98a86' #\后面跟Unicode编码表示字符串
print(t1)

r1 = r'\'hello\'' #如果不希望字符串转义，可以加上r
r2 = r'\n\\hello\\\n'
print(r2)

'''使用+来实现字符串拼接，使用*重复使用字符串，使用in和not in 判断字符串是否存在，使用[:]进行切片运算'''
e1 = 'hello '*3
print(e1)
e2 = 'me'
e1 += e2
print(e1)
print('ee'in e1)
print('ee' not in e1)
e3 = 'qwe1234'
print(e3[:])
print(e3[2])
print(e3[2:4])
print(e3[::2])
print(e3[::-1])
print(e3[3::-1])

'''处理字符串'''
str1 = ' wo ai ni '
print(len(str1)) #计算字符串长度
print(str1.capitalize()) #字符串首字母大写
print(str1.title()) #每个字母首字母大写
print(str1.upper())#每个字母都大写
print(str1.find('o'))#查找字符串所在的位置
print(str1.startswith('wo'))#检查字符串是否已该字母开头
print(str1.center(10,'*'))#将字符串以指定的宽度靠右放置左侧填充指定的字符
print(str1.isdigit())
print(str1.isalnum())#检查是否已数字字母组成
print(str1.strip())# 获得字符串修剪左右两侧空格之后的拷贝

'''格式化字符串'''
a, b = 5, 10
print('%d * %d = %d' % (a, b, a * b))
print('{0} * {1} = {2}'.format(a, b, a * b))
print(f'{a} * {b} = {a * b}')

'''列表'''
list1 = [1, 3, 5, 7]
list2 = ['love'] * 3
print(list2)
print(list1[0])
#循环遍历下标
for index in range(len(list1)):
    print(list1[index])
#循环遍历列表元素
for elem in list1:
    print(elem)
# 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
for index, elem in enumerate(list1):
    print(index, elem)

'''列表元素操作'''
list1 = [1, 3, 5, 7, 100]
# 添加元素
list1.append(200)
list1.insert(1, 400)
# 合并两个列表
# list1.extend([1000, 2000])
list1 += [1000, 2000]
print(list1) # [1, 400, 3, 5, 7, 100, 200, 1000, 2000]
print(len(list1)) # 9
# 先通过成员运算判断元素是否在列表中，如果存在就删除该元素
if 3 in list1:
	list1.remove(3)
if 1234 in list1:
    list1.remove(1234)
print(list1) # [1, 400, 5, 7, 100, 200, 1000, 2000]
# 从指定的位置删除元素
list1.pop(0)
list1.pop(len(list1) - 1)
print(list1) # [400, 5, 7, 100, 200, 1000]
# 清空列表元素
list1.clear()
print(list1) # []

'''列表切片操作'''
fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
# 列表切片
fruits2 = fruits[1:4]
print(fruits2) # apple strawberry waxberry
# 可以通过完整切片操作来复制列表
fruits3 = fruits[:]
print(fruits3) # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
fruits4 = fruits[-3:-1]
print(fruits4) # ['pitaya', 'pear']
# 可以通过反向切片操作来获得倒转后的列表的拷贝
fruits5 = fruits[::-1]
print(fruits5) # ['mango', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple', 'grape']

'''列表排序'''
list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1)
# sorted函数返回列表排序后的拷贝不会修改传入的列表
# 函数的设计就应该像sorted函数一样尽可能不产生副作用
list3 = sorted(list1, reverse=True)
# 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
list4 = sorted(list1, key=len)
print(list1)
print(list2)
print(list3)
print(list4)
# 给列表对象发出排序消息直接在列表对象上进行排序
list1.sort(reverse=True)
print(list1)

'''生成器'''
f = [x for x in range(1, 10)]
print(f)
f1 = [x + y for x in 'abc' for y in '12345']
print(f1)
import sys
f3 = [x ** 2 for x in range(1, 100)]
print(sys.getsizeof(f3)) #查看占用内存的字节数
# 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
f = (x ** 2 for x in range(1, 1000))
print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
print(f)
for val in f:
    print(val)

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for val in fib(20):
        print(val)


if __name__ == '__main__':
    main()

'''元组'''
o1 = ('我',12, True)
print(o1)
#遍历元组
for mem in o1:
    print(mem)
#获取元组中的元素
print(o1[1])
#元组改成列表
o2 = list(o1)
print(o2)
o2[1] = 14
print(o2)
#将列表转成元组
fruits_list = ['apple', 'banana', 'orange']
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)

'''集合:不允许有重复元素，而且可以进行交集、并集、差集等运算'''
# 创建集合的字面量语法
set1 = {1, 2, 3, 3, 3, 2}
print(set1)
print('Length =', len(set1))
# 创建集合的构造器语法(面向对象部分会进行详细讲解)
set2 = set(range(1, 10))
set3 = set((1, 2, 3, 3, 2, 1))
print(set2, set3)
# 创建集合的推导式语法(推导式也可以用于推导集合)
set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
print(set4)
# 集合的交集、并集、差集、对称差运算
print(set1 & set2)
# print(set1.intersection(set2))
print(set1 | set2)
# print(set1.union(set2))
print(set1 - set2)
# print(set1.difference(set2))
print(set1 ^ set2)
# print(set1.symmetric_difference(set2))
# 判断子集和超集
print(set2 <= set1)
# print(set2.issubset(set1))
print(set3 <= set1)
# print(set3.issubset(set1))
print(set1 >= set2)
# print(set1.issuperset(set2))
print(set1 >= set3)
# print(set1.issuperset(set3))

'''字典'''
age = {'小明':18, '小红':12, '小米':13}
print(age)
#创建字典
item1 = dict(a=1,b=2,c=3)
print(item1)
# 通过zip函数将两个序列压成字典
items2 = dict(zip(['a', 'b', 'c'], '123'))
print(items2)
#字典推导式
import random
randomdict = {i : random.randint(10, 100) for i in range(1, 5)}
print(randomdict)
#字典遍历
for i in age:
    print(f'{i}:{age[i]}')
#更新字典
age['小老板']=19
age.update(小老板=19)
print(age)
if '小米' in age:
    print(age['小米'])
print(age['小明'])
print(age.get('小米', 20))
print(age)
#删除字典元素
print(age.popitem())

print(age.pop("小米",13))
print(age)

import os
import time


# def main():
#     content = '北京欢迎你为你开天辟地…………'
#     while True:
#         # 清理屏幕上的输出
#         os.system('cls')  # os.system('clear')
#         print(content)
#         # 休眠200毫秒
#         time.sleep(0.2)
#         content = content[1:] + content[0]
#
# if __name__ == '__main__':
#     main()

'''_当作变量使用'''
for _ in range(4):
    print(_)

import random


def generate_code(code_len=4):
    """
    生成指定长度的验证码

    :param code_len: 验证码的长度(默认4个字符)

    :return: 由大小写英文字母和数字构成的随机验证码
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code
print(generate_code())

#返回列表中最大和第二大的值
def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2
print(max2([1,4,6,13]))


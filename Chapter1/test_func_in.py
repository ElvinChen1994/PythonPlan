# -*- coding:utf-8 -*-
# @Time: 2021/8/25 下午9:59
# @Author: Elvin

'''
过滤函数：filter(function,iterable) 返回可迭代对象
'''
def lists_filter(a):
    return a % 2 == 1

tmplist = filter(lists_filter,[1,3,4,7,12])
print(tmplist)
newlist = list(tmplist)
print(newlist)

'''
迭代函数：iter(object,sentinel) 
'''
list_l = [2,4,5]
for i in iter(list_l):
    print(i)


'''
map(function,iterable) 函数和一个或多个序列
'''

def percet(x):
    return x ** 2

print(map(percet,[1,2,4,8]))

#使用lambda
print(map(lambda x: x ** 2,[1,2,3,4]))


'''
next()返回迭代器的下一个内容，next()与iter()使用
'''
iter_list = iter([2,3,5,8])
while True:
    try:
        x = next(iter_list)
        print("执行次数：", x)
    except StopIteration:
        break

'''
sort([cmp[,key[,reverse]]])
sorted(iterable[,cmp[,key[,reverse]]])
cmp为用户定义的任何比较参数，默认None
key带一个参数的函数，为每个元素提供比较值
默认None
reverse排序结果是否反转
sorted作用域任意可迭代的对象，sort作用与列表
'''
data = [{'name':'xiaoming', 'age':18},{'name':'xiaowang', 'age':10}]

print(sorted(data, key=lambda x:(x['name'], -x['age'])))


'''
1.不可变类型：number、str、tuple
2.可变类型：list、dict、set
3.获取可变对象和不可变对象的内存地址使用id()
'''
str_id = 'word'
str_id1 = 'word'

print(id(str_id))
print(id(str_id1))
print(str_id is str_id1)

#可变对象:内存地址不一致，值一致
dict_key = {"key":"1"}
dict_key2 = {"key":"1"}

print(id(dict_key))
print(id(dict_key2))
print(dict_key2 is dict_key)
print(dict_key == dict_key2)

'''
浅拷贝：构造一个新的复合对象并将从原对象中发现的引用插入该对象中.实现的方式切片、copy模块、工厂函数
深拷贝：构造一个新的复合对象，但是遇到引用会继续递归拷贝其所指向的具体内容，也就是说它会针对引用所指向的对象继续执行拷贝，
因此产生的对象不受其他引用对象操作的影响使用deepcopy()操作
'''
#浅拷贝：不可变对象修改值后，对象的指向没有改变，可变对象值不变，对象地址指向没有改变
import copy

data_in = [2, "where", [1,4], {"key":"33"}]

data_copy = copy.copy(data_in)

print(id(data_in))
print(id(data_copy))
print(id(data_in[3]))
print(id(data_copy[3]))

data_in[0] = 3
print(data_in)
print(data_copy)

data_in[2][1] = 5
print(data_in)
print(data_copy)
print(id(data_copy[2]))
print(id(data_in[2]))

#深拷贝：深拷贝不管是修改对象的内部值，生成一个新的对象，对象地址都是不一致的，对象的元素不会影响到拷贝的对象中的元素

data_in = [2, "where", [1,4], {"key":"33"}]

data_copy = copy.deepcopy(data_in)

print(id(data_in))
print(id(data_copy))

print(id(data_copy[2]))
print(id(data_in[2]))

data_in[2][1] = 6
print(data_in)
print(data_copy)
print(id(data_copy[2]))
print(id(data_in[2]))

#赋值语句与浅拷贝的区别，虽然都指向一个内存地址，但是赋值没有创建新的容器
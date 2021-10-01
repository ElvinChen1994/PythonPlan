# -*- coding:utf-8 -*-
# @Time: 2021/10/1 下午6:09
# @Author: Elvin
from collections import Counter #字典的子类

a1 = Counter() #创建空对象
a2 = Counter('this is book') #从一个可迭代对象中创建
a3 = Counter(age=13, gen= 2)

print(a2)
print(a3)

a2.update('you')
print(a2['k'])

a2.subtract('o')
print(a2['o'])  #update方法用来新增计数， subtract方法用来减少计数

#elements()返回迭代器

b1 = Counter('you are student')
print(list(b1.elements()))

a4 = Counter('every day')
print(a4.most_common(3)) #返回计数的数据，列表中元素是元组


'''
ChainMap可以将多个字典组合
'''
name_item = {
    'name': 'xiaoming'
    }

name_item_inter = {
    'age': 12
}

from collections import ChainMap

union = ChainMap(name_item, name_item_inter)

print(type(union))

for key, value in union.items():
    print(key, value)


from collections import OrderedDict


'''
OrderedDict实现有序字典
'''
order_dict = OrderedDict()

order_dict[1] = 1
order_dict['a'] = 2
order_dict['0'] = 3

for key, value in order_dict.items():
    print(key, value)

print("*"*20)
order_dict.move_to_end(1)

for key, value in order_dict.items():
    print(key, value)


'''
deque双端队列和栈
'''

from collections import deque


class DoubleQueue():
    def __init__(self):
        self.queue = deque()

    def is_empty(self):
        """
        判断是否为空队列
        :return:
        """
        return len(self.queue) == 0

    def insert_front(self, data):
        """
        从队首插入数据
        :param data:
        :return:
        """
        self.queue.appendleft(data)

    def insert_rear(self, data):
        """
        从队尾插入数据
        :param data:
        :return:
        """
        self.queue.append(data)

    def delete_front(self):
        """
        从队首删除数据
        :return:
        """
        return self.queue.popleft()

    def delete_rear(self):
        """
        从队尾删除数据
        :return:
        """
        return self.queue.pop()

    def size(self):
        """
        返回队列长度
        :return:
        """
        return len(self.queue)

dq = DoubleQueue()
#print(dq.is_empty())
dq.insert_front(4)
dq.insert_rear(5)

print(dq.size())

'''
栈
'''
from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, data):
        """
        入栈
        :param data:
        :return:
        """
        self.stack.append(data)

    def pop(self):
        """
        出栈
        :return:
        """
        return self.stack.pop()

    def size(self):
        """
        栈大小
        :return:
        """
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0


stack = Stack()

stack.push(4)
stack.push(3)
stack.push(1)

print(stack.pop())
print(stack.size())
# -*- coding:utf-8 -*-
# @Time: 2021/8/18 9:50 上午
# @Author: Elvin
'''反射'''

class Feel:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.gen = '男'

    def show(self):
        return '%s~%s~%s'%(self.name, self.age, self.gen)

feel = Feel('wangming', 12)
func = getattr(feel, 'show')
print(func)
print(func())
print(hasattr(feel, 'name')) #判断对象中是否存在该属性
setattr(feel, 'name', 'lihua')
print(feel.name)
delattr(feel, 'gen')

#模块级别的反射，从模块中取对象

import Chapter3.test_attr_data

inp = input('请输入：')
if hasattr(Chapter3.test_attr_data, inp):
    func = getattr(Chapter3.test_attr_data, inp)
    print(func())
else:
    print('error')
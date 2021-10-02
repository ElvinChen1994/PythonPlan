# -*- coding:utf-8 -*-
# @Time: 2021/10/1 下午10:32
# @Author: Elvin

from functools import singledispatch

class Stu(object):
    def __init__(self, name):
        self.name = name

    def wake_up(self):
        print('起床')

class Police(object):
    def __init__(self, name):
        self.name = name

    def wake_up(self):
        print('起床')

@singledispatch  #实现泛型函数
def wake_up(obj):
    print('不处理')


@wake_up.register(Stu)
def wake_stu(obj):
    print('今天周末休息,让孩子们再睡一会')


@wake_up.register(Police) #注册一个类型来装饰函数
def wake_police(obj):
    print('警察很辛苦,又要起床了')
    obj.wake_up()


stu = Stu('小明')
police = Police('小明爸爸')

wake_up(stu)
wake_police(police)
wake_up('一个字符串')



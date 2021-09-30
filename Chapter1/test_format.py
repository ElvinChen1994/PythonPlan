# -*- coding:utf-8 -*-
# @Time: 2021/9/30 下午8:37
# @Author: Elvin

'''
格式化方法：%格式化，format方法格式化，fstring格式化。

%s 字符串 (采用str()的显示)

%r 字符串 (采用repr()的显示)

%c 单个字符

%b 二进制整数

%d 十进制整数

%i 十进制整数

%o 八进制整数

%x 十六进制整数

%e 指数 (基底写为e)

%E 指数 (基底写为E)

%f 浮点数
'''
log = "{}-{}-{}"
print(log.format(1, 'bug', '测试'))

#%操作符使用
format_test = "my name is %s. i'm %d years old"
string_test = format_test % ('xiaowang', 22)
print(string_test)

#format使用
log = "{id}-{type}-{msg}"
print(log.format(id=1,type='bug',msg=u'测试'))

#字典格式化
item_demo = {
    'id' : 12,
    'type':"test",
    'msg':u'测试'
}

test1 = "{0[id]}-{0[type]}-{0[msg]}".format(item_demo)
print(test1)

test2 = "{item_demo[id]}-{item_demo[type]}-{item_demo[msg]}".format(item_demo=item_demo)
print(test2)

"tuple格式化"
tuple_demo = (2,'test',u'测试')

test3 = "{0[0]}-{0[1]}-{0[2]}".format(tuple_demo)
print(test3)

test4 = "{tuple_demo[0]}-{tuple_demo[1]}-{tuple_demo[2]}".format(tuple_demo=tuple_demo)
print(test4)

#对象格式化
class data_info(object):
    def __init__(self, id, type, msg):
        self.id = id
        self.type = type
        self.msg = msg

data_in = data_info(12, 'bug', u'测试')
log = "{data_in.id}-{data_in.type}-{data_in.msg}".format(data_in=data_in)
print(log)

#f-string

color = 'red'
string = f"I like {color.upper()}"
print(string)
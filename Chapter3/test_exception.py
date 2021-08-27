# -*- coding:utf-8 -*-
# @Time: 2021/8/17 4:33 下午
# @Author: Elvin
try:
    #代码块，逻辑
    input_aa= input('请输入：')
    i = int(input_aa)
except Exception as e:
    #代码如果出错执行当前块的内容
    #e是Exception对象，对象中封装了错误信息
    i = 1
print(i)

#指定异常的类型
try:
    li = [11, 22]
    li[2]
except IndexError as e:
    print(e)

'''
    常见的异常：
    1.AttributeError 访问对象没有属性
    2.ImportError 导入包异常
    3.IndentationError 语法错误，代码没有对齐
    4.IndexError 下标索引超出序列边界
    5.NameError 使用一个还未被赋予对象的变量
    6.TypeError 传入对象类型与要求不符合
    7.UnboundLocalError 试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量
    8.ValueError 传入一个调用者不期望的值，即使值是争取的
    9.UnicodeError 编码的相关错误
    10.TabError Tab和空格混用
    11.MemoryError 计算机的内存溢出错误
    12.OverflowError 数值运算超出最大限制
    
'''

try:
    pass
except NameError as e:
    #只捕捉NameError的错误类型
    print('错误的信息是：', e)
except Exception as e:
    #捕捉全部的错误类型
    print('错误的信息是：', e)
except:
    #捕捉全部的错误类型，但没有错误信息
    print('错误：')
else:
    print('如果没有异常就执行此处的代码')
finally:
    print('不管是否有异常都会执行此处的代码')

#主动触发异常
try:
    raise Exception('异常是...')
except Exception as e:
    print(e)


'''自定义异常：由关键字raise实现，关键词后面填写异常和异常信息'''
class NewError(Exception):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

#obj = NewError('你错了')
#print(obj)


try:
    raise NewError('错了') #等同与#obj = NewError('你错了')
except NewError as e:
    print(e) #e对象的__str__()，获取返回

class MyError(Exception):
    pass

if __name__ == '__main__':
    try:
        #抛出自定义异常
        raise MyError('自定义异常')
    #捕捉自定义异常
    except MyError as e:
        print('异常是：', e)


'''嵌套异常'''
try:
    1 / 2 == 0
except Exception as e:
    try:
        print('第一个错误：', e)
        3 / 3 == 1
    except Exception as a:
        print('第二个错误: ', a)


def retruntest(a):
    try:
        if a <= 0:
            raise ValueError("data not in")
        else:
            return a
    except ValueError as e:
        print(e)

    finally:
        print("end...")
        return -1
'''
finally中使用retrun语句进行返回，可能会出现问题
'''
print(retruntest(0))
print(retruntest(2))

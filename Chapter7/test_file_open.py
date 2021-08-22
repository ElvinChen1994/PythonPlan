# -*- coding:utf-8 -*-
# @Time: 2021/8/22 下午4:24
# @Author: Elvin

'''
filename: 包含访问文件名称的字符串值
access:打开文件的模式，默认访问只读r
buffering:如果buffing设置值为0，就不会寄存；如果值取1，访问文件时就会寄存行，如果设置
大于1，表示寄存区缓冲的大小；如果去负值，寄存去的缓冲大小就是系统的默认值
newline: 区分换行符
closefd: 传入的file参数类型
opener: 设置自定义开启器，开启器的返回值必须是一个打开的文件描述符。
'''

path = '/Users/macintoshhd/PycharmProjects/PythonPlan/Chapter7/test_elvin'
f_name = open(path)
#输出文件名
print(f_name.name)

'''
流（Stream）是一个很重要的概念。可以把流想象成一根水管，数据就是水管里的水，但是只能单向流动。
Input Stream就是数据从外面（磁盘、网络）流进内存，Output Stream就是数据从内存流到外面去

'''

#读取文件

path = '/Users/macintoshhd/PycharmProjects/PythonPlan/Chapter7/test_elvin'
f_name = open(path,'r')
print(f'read result:{f_name.read(12)}') #读取文件从头开始的字符串数量

#写入文件
f_name = open(path,'w')
print(f"write length:{f_name.write('wo ai ni')}")  #写入时覆盖原有的内容

#写入追加
f_name = open(path,'a')
print(f"write length:{f_name.write('我来哦了')}")

'''
如果传递给open函数的文件名不存在，写模式（w）和追加模式（a）就会创建一个新的空文件，然后执行写入或追加
'''
#写入文件换行
path = '/Users/macintoshhd/PycharmProjects/PythonPlan/Chapter7/test_elvin'
f_name = open(path,'a')
print("add length:",{f_name.write('\n我来哦了')})

'''
文件格式：若需要读或写特定编码方式的文本，则需要给open函数传入encoding参数；若需要读取GBK编码的文件，
则前面的示例可以改写为f_name=open(path, 'r', encoding='gbk')，这样读取到的文件就是GBK编码方式的文件了。
'''

#读取一行
path = '/Users/macintoshhd/PycharmProjects/PythonPlan/Chapter7/test_elvin'
f_name = open(path,'r')
print(f'readline: {f_name.readline()}')

#读取所有并返回列表，当传入的数值小于等于列表中一个字符串的长度值时，该字符串会被读取；当传入小于等于0的数值时，所有字符都会被读取
path = '/Users/macintoshhd/PycharmProjects/PythonPlan/Chapter7/test_elvin'
f_name = open(path,'r')
#str_list = ['gell','wwd']
print(f'readline: {f_name.readlines()}')

#向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。
path = '/Users/macintoshhd/PycharmProjects/PythonPlan/Chapter7/test_elvin'
f_name = open(path,'r')
str_list = ['gell','wwd']
print(f'readline: {f_name.writelines(str_list)}')

#关闭文件
path = '/Users/macintoshhd/PycharmProjects/PythonPlan/Chapter7/test_elvin'
f_name = open(path,'w')
print(f"write:{f_name.write('hello l love you')}")
f_name.close()

with open(path,'w') as f: #自动调用close方法
    f_name = open(path,'w')
    print(f"write data:{f_name.write('ni hao wei lai')}")

import os
#os.rename(current_file_name, new_file_name)
#os为导入的os模块，current_file_name为当前文件名，new_file_name为新文件名。若文件不在当前目录下，则文件名需要带上绝对路径。

#os.remove(file_name) 移除文件

'''
file对象的属性
'''
file = open(path,'r')
file.close()
print("文件名是：",file.name)
print("是否关闭：",file.closed)
print("访问模式：",file.mode)

#文件定位
file = open(path,'r+')
str = file.read(5)
print("读取的字符串是：",str)

#查询当前位置
position = file.tell()
print('文件当前位置：',position)

# 把指针再次重新定位到文件开头
pose = file.seek(0,0)
str=file.read(4)
print("重新读取字符串：",str)

#删除目录
r=os.rmdir('/Users/macintoshhd/PycharmProjects/PythonPlan/Chapter8/test')
print(r)

file_data = open(path,"r")
fl = file_data.fileno()
print("文件内容是：", fl)

#循环执行
file = open(path,'r+')

for index in range(3):
    line = file.readline()
    print("这是 %d 行 - %s" % (index,line))

file.close()

#文件截取
file = open(path,'r+')

line = file.readline()
print('读取第一行: ', line)

file.truncate()

line = file.readline()
print("读取数据：%s" % (line))
file.close()

file = open(path,'w+')

line = file.readline()
print('读取第一行: ', line)

file.truncate(2)

line = file.readline()
print("读取数据：%s" % (line))
file.close()

#循环读取每一行,懒加载迭代
f_name = open(path)
while True:
    line = f_name.readline()
    if not line:
        break
    print(f'read line is:{line}')
f_name.close()

#使用fileinput迭代
import fileinput


for line in fileinput.input(path):
    print(f'line is:{line}')
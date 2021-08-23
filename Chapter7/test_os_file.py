# -*- coding:utf-8 -*-
# @Time: 2021/8/22 下午11:58
# @Author: Elvin
import os

# path=['/Users/macintoshhd/PycharmProjects/PythonPlan/Chapter7/test_elvin_file.txt',
#       '/Users/macintoshhd/PycharmProjects/PythonPlan/Chapter7/test_file_open.py',
#       '/Users/macintoshhd/PycharmProjects/PythonPlan/123.py']

path='/Users/macintoshhd/PycharmProjects/PythonPlan/Chapter7/test_elvin_file.txt'
path = 'test_elvin_file.txt'
s = os.path.abspath(path) #	返回绝对路径
print(s)

s = os.path.basename(path) #返回文件名称
print(s)

r = os.path.commonprefix(path) #path共有的最长的路径
print(r)

r = os.path.dirname(path) #返回文件路径
print(r)

r = os.path.exists(path) #返回文件是否存在
print(r)

r = os.path.realpath(path) #返回真是的路径
print(r)

#目录和文件合并成一个路径
r = os.path.join('/Users/macintoshhd/PycharmProjects/PythonPlan','test_elvin_file.txt')
print(r)

r = os.path.split(path) #分割目录，返回一个元组
print(r)
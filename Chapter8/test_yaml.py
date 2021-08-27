# -*- coding:utf-8 -*-
# @Time: 2021/8/27 下午5:29
# @Author: Elvin
'''
1.大小写
2.缩进表示层级关系
3.缩进只允许是用空格
4.相同元素层级元素左侧对齐

支持的数据结构：
对象：映射、hash、dict
数组：序列、列表
纯量：:字符串、布尔值、整数、浮点数、Null、时间、日期
'''
import os
import yaml
# print(os.path.split(os.path.realpath(__file__))[0])

curPath = os.path.dirname(os.path.realpath(__file__))
#curPath = os.path.dirname(os.path.realpath(__file__)) + '/Chapter8'

print(curPath)
yamlPath = os.path.join(curPath,"test_data.yaml")
print(yamlPath)

f = open(yamlPath, 'r')
read_data = f.read()
print(read_data)

s = yaml.load(read_data, Loader=yaml.FullLoader) #通过默认加载​​器（FullLoader）禁止执行任意函数
print(s)
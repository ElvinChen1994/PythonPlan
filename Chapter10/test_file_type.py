# -*- coding:utf-8 -*-
# @Time: 2021/10/13 下午6:33
# @Author: Elvin
'''
ini格式文件导入
'''

from configparser import ConfigParser

conf = ConfigParser()
conf.read("test_mysql.ini")

print(conf.sections())
print(conf.options("mysql"))
print(conf.items("mysql"))
print(conf.get("mysql", "port"))
print(conf.getint("mysql", "password"))

'''
yaml格式文件
'''
import yaml

file_mysql = open('/Users/macintoshhd/PycharmProjects/PythonPlan/Chapter10/test_mysql.yaml')
data = file_mysql.read()
print(data)
yaml_reader = yaml.load(data, Loader=yaml.FullLoader)
print(yaml_reader['mysql'])

'''
xml格式文件
'''
import xml.dom.minidom

dom = xml.dom.minidom.parse('/Users/macintoshhd/PycharmProjects/PythonPlan/Chapter10/test_xml')
test = dom.documentElement
print(test.nodeName)

mysql_node = test.getElementsByTagName('mysql')[0]
for node in mysql_node.childNodes:
    if node.nodeType == 1:
        print(node.nodeName, node.firstChild.data)
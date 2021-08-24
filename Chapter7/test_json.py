# -*- coding:utf-8 -*-
# @Time: 2021/8/23 下午10:13
# @Author: Elvin

'''
json.dumps():对数据进行编码
json.loads():对数据进行解码
'''

import json

data = {'id':100, 'name':'xiao hu'}
#编码python>json
json_data = json.dumps(data)
print(f'初始数据：{data}')
print(f'json对象: {json_data}')

#解码json>python
json_data1 = json.loads(json_data)
print(f"json_data1['id']:{json_data1['id']}")

#文件处理：写入json数据
path='/Users/macintoshhd/PycharmProjects/PythonPlan/Chapter7/'
with open(path,'w') as f:
    json.dump(data,f)

#文件处理：写入json数据
with open(path,'r') as f:
    data = json.load(f)
    print(data)

import os

for item in os.listdir(path):
    print(item)

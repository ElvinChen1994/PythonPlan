# -*- coding:utf-8 -*-
# @Time: 2021/7/25 11:10 下午
# @Author: Elvin

username = input('请输入用户名: ')
password = input('请输入密码: ')

if username == 'admin' and password == '11111':
    print('验证成功!')
else:
    print('验证失败!')
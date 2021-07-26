# -*- coding:utf-8 -*-
# @Time: 2021/7/25 11:10 下午
# @Author: Elvin


"""验证身份逻辑"""
username = input('请输入用户名: ')
password = input('请输入密码: ')

if username == 'admin' and password == '11111':
    print('验证成功!')
else:
    print('验证失败!')


"""分数计算"""
score = float(input('请输入班级分数：'))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = 'E'
print('对应的等级是：', grade)
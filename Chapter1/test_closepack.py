# -*- coding:utf-8 -*-
# @Time: 2021/8/24 下午11:21
# @Author: Elvin
def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent
    return exponent_of # 返回值是 exponent_of 函数
square = nth_power(2) # 计算一个数的平方
cube = nth_power(3) # 计算一个数的立方
son = nth_power(4)
print(square(2))  # 计算 2 的平方
print(cube(2)) # 计算 2 的立方
print(son())


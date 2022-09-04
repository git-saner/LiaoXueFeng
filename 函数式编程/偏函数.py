# -*- coding : utf-8 -*-
# @Time : 2022/9/4 20:20
# @Author : Saner
# @File : 偏函数.py
# @Software : PyCharm
'''
 1.当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。

'''
import functools

print(int('12345', base=8))

max2 = functools.partial(max, 100)

print(max2(1, 2, 3.4))

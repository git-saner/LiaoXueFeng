# -*- coding : utf-8 -*-
# @Time : 2022/9/4 9:44
# @Author : Saner
# @File : 返回函数.py
# @Software : PyCharm

def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            # # 用g函数的参数绑定循环变量当前的值
            # def g():
            #     return j * j

            return lambda: j * j

        fs.append(f(i))
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())


def inc():
    x = 0

    def fn():
        nonlocal x  # 解释器把fn()的x看作外层函数的局部变量
        x = x + 1
        return x

    return fn


f = inc()
print(f())  # 1
print(f())  # 2

# -*- coding : utf-8 -*-
# @Time : 2022/9/4 10:10
# @Author : Saner
# @File : 装饰器.py
# @Software : PyCharm
import time

'''
def log(text):
    def decorate(func):
        def wrapper(*args, **kw):
            print("%s %s()" % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorate


@log('execute')
def now():
    # 打印格式化时间
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))  # 打印按指定格式排版的时间


now()
print(now.__name__, end="")
'''


# 设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
def metric(fn):
    def wrapper(*args, **kw):
        print("函数执行时间为%s" % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
        return fn(*args, **kw)

    # print('%s executed in %s ms' % (fn.__name__, 10.24))
    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

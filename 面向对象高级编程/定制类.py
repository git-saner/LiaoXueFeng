# -*- coding : utf-8 -*-
# @Time : 2022/9/5 14:47
# @Author : Saner
# @File : 定制类.py
# @Software : PyCharm
'''
    1.直接显示变量调用的不是__str__()，而是__repr__()，
    两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，
    也就是说，__repr__()是为调试服务的。
    2.

'''


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b

        if self.a > 1000:
            raise StopIteration()
        else:
            return self.a

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a

        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            L = []
            a, b = 1, 1
            if start is None:
                start = 0
            for k in range(stop):
                if k >= start:
                    L.append(a)
                a, b = b, a + b
            return L


class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Student Object (name:%s)" % self.name

    def __getattr__(self, item):
        if item == 'score':
            return 100
        if item == 'age':
            return lambda: 25


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


if __name__ == '__main__':
    pass
    # for n in Fib():
    #     print(n)
    # f = Fib()
    # print(f[0])
    # print(f[0:5])
    #
    # print(Student('Michael').score)
    # print(Student('Michael').age())

    print(Chain().status.user.timeline.list)

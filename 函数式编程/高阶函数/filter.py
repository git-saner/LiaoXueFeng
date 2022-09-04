# -*- coding : utf-8 -*-
# @Time : 2022/9/4 9:17
# @Author : Saner
# @File : filter.py
# @Software : PyCharm


def __odd__iter():
    n = 1
    while True:
        n = n + 2
        yield n


def __filter__condition(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = __odd__iter()
    while True:
        n = next(it)
        yield n
        it = filter(__filter__condition(n), it)


for n in primes():
    if n < 1000:
        print(n)
    else:
        break

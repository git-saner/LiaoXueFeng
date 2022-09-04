# -*- coding : utf-8 -*-
# @Time : 2022/9/4 8:34
# @Author : Saner
# @File : map-reduce.py
# @Software : PyCharm

from functools import reduce

digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def char2num(s):
        return digits[s]

    def f(x, y):
        return x * 10 + y

    return reduce(f, map(char2num, s))


print(str2int('213123'))
print(int('213123'))

# -*- coding : utf-8 -*-
# @Time : 2022/9/6 11:16
# @Author : Saner
# @File : 错误处理.py
# @Software : PyCharm

from functools import reduce


def str2num(s):
    if s.find('.'):
        return float(s)
    else:
        return int(s)


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


if __name__ == '__main__':
    try:
        main()
    except BaseException as e:
        print("Exception:", e)
    pass

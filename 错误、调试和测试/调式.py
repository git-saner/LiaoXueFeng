# -*- coding : utf-8 -*-
# @Time : 2022/9/6 14:21
# @Author : Saner
# @File : 调式.py
# @Software : PyCharm
import logging
import pdb

logging.basicConfig(level=logging.INFO)


def foo(s):
    n = int(s)
    # assert n != 0, 'n is zero'
    # logging.info('n = %d' % n)
    pdb.set_trace()
    print('hello')
    print(10 / n)


if __name__ == '__main__':
    pass
    foo('0')

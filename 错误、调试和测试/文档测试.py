# -*- coding : utf-8 -*-
# @Time : 2022/9/6 15:24
# @Author : Saner
# @File : 文档测试.py
# @Software : PyCharm

def fact(n):
    '''
    >>> fact(1)
    1
    >>> fact(10)
    3628800
    >>> fact(-1)
    Traceback (most recent call last):
        ...
    ValueError
    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    pass

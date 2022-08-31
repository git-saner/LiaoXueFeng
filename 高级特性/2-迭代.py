# -*- coding : utf-8 -*-
# @Time : 2022/8/31 16:21
# @Author : Saner
# @File : 2-迭代.py
# @Software : PyCharm

'''
    请使用迭代查找一个list中最小和最大值，并返回一个tuple：
'''


def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)

    min_num, max_num = L[0], L[0]
    for num in L:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num

    return (min_num, max_num)


if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

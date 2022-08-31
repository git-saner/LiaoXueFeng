# -*- coding : utf-8 -*-
# @Time : 2022/8/31 10:46
# @Author : Saner
# @File : 1-切片.py
# @Software : PyCharm

'''
利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
'''


def trim(s):
    while len(s) >= 1 and s[0] == ' ':
        s = s[1:]
    while len(s) >= 1 and s[-1] == ' ':
        s = s[:-1]
    return s


if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

print("-" * 30)
str = ' '
print("str=%s" % str[1:])
print("str=%s" % str[:-1], end="")

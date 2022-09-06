# -*- coding : utf-8 -*-
# @Time : 2022/9/6 17:01
# @Author : Saner
# @File : 文件读写.py
# @Software : PyCharm
fpath = r'D:\PycharmProjects\LiaoXueFeng\IO编程\text.txt'

if __name__ == '__main__':
    with open(fpath, 'r') as f:
        s = f.read()
        print(s)
        print(type(s))

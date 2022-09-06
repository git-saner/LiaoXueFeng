# -*- coding : utf-8 -*-
# @Time : 2022/9/6 17:18
# @Author : Saner
# @File : SBIO.py
# @Software : PyCharm
from io import StringIO, BytesIO


def WSIO():
    f = StringIO()
    f.write('hello,world!')
    print(f.getvalue())


def RSIO():
    f = StringIO('Hello!\nHi!\nGoodBye!')
    while True:
        s = f.readline()
        if s == '':
            break
        print(s.strip())


def WBIO():
    f = BytesIO()
    f.write("你好".encode('utf-8'))
    print(f.getvalue())


def RBIO():
    f = BytesIO(b'\xe4\xbd\xa0\xe5\xa5\xbd')
    print(f.read().decode(encoding='utf-8'))


if __name__ == '__main__':
    WSIO()
    RSIO()
    WBIO()
    RBIO()
    pass

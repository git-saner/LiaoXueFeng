# -*- coding : utf-8 -*-
# @Time : 2022/9/6 17:44
# @Author : Saner
# @File : 操作文件和目录.py
# @Software : PyCharm
import os

if __name__ == '__main__':
    # 操作系统类型
    print(os.name)
    # 所有环境变量
    print(os.environ)
    # 获取某个环境变量的值
    print(os.environ.get('PATH'))
    # 当前绝对路径
    print(os.path.abspath('.'))
    # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
    # print(os.path.join('D:\PycharmProjects\LiaoXueFeng\IO编程', 'testdir'))
    # 然后创建一个目录:
    # print(os.mkdir(r'D:\PycharmProjects\LiaoXueFeng\IO编程\testdir'))
    # 删除一个目录
    # print(os.rmdir(r'D:\PycharmProjects\LiaoXueFeng\IO编程\testdir'))
    # 拆分路径
    print(os.path.split(r'D:\PycharmProjects\LiaoXueFeng\IO编程\testdir'))
    # 获取文件拓展名
    print(os.path.splitext(r'D:\PycharmProjects\LiaoXueFeng\IO编程\SBIO.py')[1])
    # 重命名
    # print(os.rename('test.py', 'test1.py'))
    # 删除文件
    # print(os.remove('test1.py'))
    # shutil模块提供了copyfile()的函数
    # 列出当前目录下所有目录
    print([x for x in os.listdir('.') if os.path.isdir(x)])
    # 列出当前目录下所有.py文件
    print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

    pass

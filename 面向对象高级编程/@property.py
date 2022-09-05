# -*- coding : utf-8 -*-
# @Time : 2022/9/5 14:47
# @Author : Saner
# @File : @property.py
# @Software : PyCharm
'''
    1.Python内置的@property装饰器就是负责把一个方法变成属性调用的
'''


class Screen(object):

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def resolution(self):
        return self.__width * self.__height


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

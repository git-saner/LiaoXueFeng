# -*- coding : utf-8 -*-
# @Time : 2022/9/5 14:47
# @Author : Saner
# @File : __slots__.py
# @Software : PyCharm
'''
    1.Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
    2.__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的

'''


class Student(object):
    __slots__ = ('name', 'score')


student = Student()
student.gender = 'female'

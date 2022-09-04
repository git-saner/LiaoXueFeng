# -*- coding : utf-8 -*-
# @Time : 2022/9/4 21:57
# @Author : Saner
# @File : 实例属性和类属性.py
# @Software : PyCharm

class Student(object):
    count = 0

    def __init__(self, name):
        Student.count += 1
        self.__name = name


if Student.count != 0:
    print('测试失败1!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败2!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败3!')
        else:
            print('Students:', Student.count)
            print('测试通过!')

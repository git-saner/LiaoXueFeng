# -*- coding : utf-8 -*-
# @Time : 2022/9/5 14:48
# @Author : Saner
# @File : 枚举类.py
# @Software : PyCharm

from enum import Enum, unique

Gender = Enum('Gender', ("Male", "Female"))


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')

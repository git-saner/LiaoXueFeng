# -*- coding : utf-8 -*-
# @Time : 2022/9/4 21:22
# @Author : Saner
# @File : 访问限制.py
# @Software : PyCharm
'''
    1.如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__


'''

'''
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def set__score(self, score):
        self.__score = score

    def get__score(self):
        return self.__score
'''


# 请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender == 'female' or gender == 'male':
            self.__gender = gender
        else:
            raise ValueError('invalid gender')


# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')

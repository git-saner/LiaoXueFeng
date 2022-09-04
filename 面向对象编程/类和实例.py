# -*- coding : utf-8 -*-
# @Time : 2022/9/4 21:06
# @Author : Saner
# @File : 类和实例.py
# @Software : PyCharm

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print("%s %d" % (self.name, self.score))


if __name__ == '__main__':
    bart = Student('Damian Lillard', 90)
    print(bart.name)
    bart.print_score()

# -*- coding : utf-8 -*-
# @Time : 2022/9/4 21:39
# @Author : Saner
# @File : 继承和多态.py
# @Software : PyCharm


class Human(object):
    def run(self):
        print("human is running")


class Cat(Human):
    def run(self):
        print("cat is running ")


def run_twice(object):
    object.run()
    object.run()


cat = Human()
human = Human()

run_twice(cat)
run_twice(human)

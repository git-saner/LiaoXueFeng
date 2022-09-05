# -*- coding : utf-8 -*-
# @Time : 2022/9/5 14:47
# @Author : Saner
# @File : 多重继承.py
# @Software : PyCharm
'''
    由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。
    只允许单一继承的语言（如Java）不能使用MixIn的设计
'''


class Animal(object):
    pass


class Mammal(Animal):
    def giveBirth(self):
        print("胎生")


class Runnable(object):
    def run(self):
        print("running")


class Dog(Mammal, Runnable):
    pass


dog = Dog()
dog.giveBirth()
dog.run()

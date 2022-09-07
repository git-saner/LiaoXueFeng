# -*- coding : utf-8 -*-
# @Time : 2022/9/6 18:13
# @Author : Saner
# @File : 序列化.py
# @Software : PyCharm
'''
    1.pickle只能用于Python
    2.
'''

# 引入pickle 模块
import pickle

import json


def writeBytes():
    d = dict(name='Michael', age=20)
    # 把任意对象序列表成一个bytes
    pickle.dumps(d)

    f = open('dump.txt', 'wb')
    # 将bytes写入文件
    pickle.dump(d, f)
    f.close()


def readBytes():
    f = open('dump.txt', 'rb')
    d = pickle.load(f)  # 反序列化出对象
    f.close()
    print(d)


def Json():
    d = dict(name='Michael', age=20)
    print(json.dumps(d))  # 将python对象转化为json格式,返回一个str
    json_str = '{"name": "Michael", "age": 20}'
    print(json.loads(json_str))  # 将json的字符串反序列化


def JsonAdvanced():
    stu = Student('Michael', 21)
    # default参数就是把任意一个对象编程一个可序列化的JSON对象
    print(json.dumps(stu, default=Student2Dict))
    print(json.dumps(Student2Dict(stu)))

    json_str = '{"name": "Michael", "age": 25}'
    # json.loads 负责json数据转化为dict对象,object_hook传入将dict转化为Student对象的参数
    print(json.loads(json_str, object_hook=Dict2Student))
    pass


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


def Student2Dict(obj):
    return {
        'name': obj.name,
        'age': obj.age
    }


def Dict2Student(d):
    return Student(d['name'], d['age'])


def exercise():
    obj = dict(name='小明', age=20)
    # json 序列化时对中文默认使用ascii编码
    s = json.dumps(obj, ensure_ascii=True)
    print(s)
    a = json.dumps(obj, ensure_ascii=False)
    print(a)


if __name__ == '__main__':
    exercise()

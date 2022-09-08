# -*- coding : utf-8 -*-
# @Time : 2022/9/8 20:00
# @Author : Saner
# @File : 多线程.py
# @Software : PyCharm

import time, threading, multiprocessing

# 假定这是你的银行存款:
balance = 0
lock = threading.Lock()
local_school = threading.local()


def process_student():
    stu = local_school.student
    print("Hello,%s (in %s)" % (stu, threading.current_thread().name))


def process_thread(name):
    local_school.student = name
    process_student()


# 测试threading.local()
def thread_local():
    # t1 = threading.Thread(target=process_thread, args=('Bob',), name='Thead-A')
    t1 = threading.Thread(target=process_thread, args=('Bob',))
    # t2 = threading.Thread(target=process_thread, args=('Alice',), name='Thead-B')
    t2 = threading.Thread(target=process_thread, args=('Alice',))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(2000000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()


def test_process_lock():
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)


def loop():
    x = 0
    while True:
        x = x ^ 1


if __name__ == '__main__':
    # for i in range(multiprocessing.cpu_count()):
    #     t = threading.Thread(target=loop)
    #     t.start()
    thread_local()
    pass

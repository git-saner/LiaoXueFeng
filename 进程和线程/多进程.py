# -*- coding : utf-8 -*-
# @Time : 2022/9/7 19:07
# @Author : Saner
# @File : 多进程.py
# @Software : PyCharm

import os, time, random
import subprocess
from multiprocessing import Process, Pool, Queue


def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


# 父进程创建子进程
def run_ChildProcess():
    print('Parent process is %s' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start')
    p.start()
    # join()等待子线程结束，继续往下运行
    p.join()
    print('Child process end')


# 单个进程
def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s run %0.2f seconds.' % (name, (end - start)))


# 运行进程池
def run_Pool():
    print('Parent process %s.' % os.getpid())
    p = Pool(8)
    for i in range(9):
        p.apply_async(long_time_task, args=(i,))
    print('Wait for all subProcess done...')
    p.close()
    p.join()
    print('All subProcess done')


# 模拟访问www.python.org
def runPythonOrg():
    print('$ nslookup www.python.org')
    r = subprocess.call(['nslookup', 'www.python.org'])
    print('Exit code:', r)


def write(q):
    print('Process to write:%s' % os.getpid())
    for value in ['a', 'b', 'c']:
        print('Put %s to queue..' % value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    print('Process to read :%s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from  queue' % value)


# 进程间通信
def Communication():
    # 父进程创建Queue,并传递给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    # 等待pw结束
    pw.join()
    print('pw 结束')
    pr.terminate()


if __name__ == '__main__':
    Communication()
    pass

import queue
import random
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()
result_queue = queue.Queue()


class QueueManger(BaseManager):
    pass


def return_task_queue():
    return task_queue


def return_result_queue():
    return result_queue


if __name__ == '__main__':
    QueueManger.register('get_task_queue', callable=return_task_queue)
    QueueManger.register('get_result_queue', callable=return_result_queue)
    manger = QueueManger(address=('127.0.0.1', 5000), authkey=b'abc')
    manger.start()
    task = manger.get_task_queue()
    result = manger.get_result_queue()
    for i in range(10):
        n = random.randint(0, 10000)
        print("Put task %d" % n)
        task.put(n)

    print("Try get results")
    for i in range(10):
        try:
            r = result.get(timeout=5)
            print("Result %s" % r)
        except queue.Empty:
            print("Result queue is empty")

    manger.shutdown()
    print("Master Exit")

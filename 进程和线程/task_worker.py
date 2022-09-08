import queue
import time
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


if __name__ == "__main__":
    QueueManager.register('get_task_queue')
    QueueManager.register('get_result_queue')
    server_addr = '127.0.0.1'
    print("Connecting to sercer %s" % server_addr)
    m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
    m.connect()
    task = m.get_task_queue()
    result = m.get_result_queue()
    for i in range(10):
        try:
            n = task.get(timeout=5)
            print("Run task %d" % n)
            r = "%d * %d = %d" % (n, n, n * n)
            time.sleep(1)
            result.put(r)
        except queue.Empty:
            print("task queue is empty")

    print("Worker Exit")

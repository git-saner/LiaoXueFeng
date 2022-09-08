# 高级特性

## 切片

`L[0:3]`表示，从索引`0`开始取，直到索引`3`为止，但不包括索引`3`。

## 迭代

迭代（Iteration）：可以通过for循环进行遍历

只要是可迭代对象，无论有无下标，都可以迭代

通过`collections.abc`模块的`Iterable`类型判断是否是可迭代对象

`isinstance(obj,Iterable)`  返回布尔型变量

可以通过`enumerate`函数实现下标

```python
>>> for i,value in enumerate(['a','b','c']):
	print(i,value)
0 a
1 b
2 c
```



## 生成器

1. 在Python中，这种一边循环一边计算的机制，称为生成器：
2. 生成器不但可以作用于`for`循环，还可以被`next()`函数不断调用并返回下一个值，直到最后抛出`StopIteration`错误表示无法继续返回下一个值了

```
g=(x*x for x in range(10))
```

## 迭代器

1. 直接作用于`for`循环的对象统称为可迭代对象：：`Iterable`
2. 可以被`next()`函数调用并不断返回下一个值的对象称为迭代器：`Iterator`
3. 生成器都是`Iterator`对象，但`list`、`dict`、`str`虽然是`Iterable`，却不是`Iterator`。把`list`、`dict`、`str`等`Iterable`变成`Iterator`可以使用`iter()`函数：
4. `Iterator`甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的

# 函数式编程

## 高阶函数

### map/reduce

### filter

### sorted

## 返回函数

## 匿名函数

## 装饰器

## 偏函数

# 面向对象高级编程

## 定制类

### __str__

`__str__()`返回用户看到的字符串，改变`print(object)` 的样式

`__repr__()`返回程序开发者看到的字符串，也就是说，`__repr__()`是为调试服务的。

```python
class Student(self):
    def __init__(self,name):
        self.name=name
	def __str__(self)：
		return "Student Object (name:%s)"%self.name
	__repr__ = __str__    

if __name__ == '__main__':
    print(Student("Michael"))
```

### __iter__

如果一个类想被用于`for ... in`循环，类似list或tuple那样，就必须实现一个`__iter__()`方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的`__next__()`方法拿到循环的下一个值，直到遇到`StopIteration`错误时退出循环。

```python
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):  # 实例本身就是迭代对象，故返回自己
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        #设置循环终止条件
        if self.a > 1000:
            raise StopIteration()
        else:
            return self.a
        
if __name__ == '__main__':
    for n in Fib():
        print(n)
```

### __getitem__

要表现得像list那样按照下标取出元素，需要实现`__getitem__()`方法：

`__getitem__()`传入的参数可能是一个int，也可能是一个切片对象`slice`，

```python
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a

        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            L = []
            a, b = 1, 1
            if start is None:
                start = 0
            for k in range(stop):
                if k >= start:
                    L.append(a)
                #无论k和start大小如何，都要执行以下语句
                a, b = b, a + b
            return L
        
if __name__ == '__main__':
    print(Fib()[0])
```

### __getattr__

1.当调用不存在的属性时，比如`score`，Python解释器会试图调用`__getattr__(self, 'score')`来尝试获得属性，这样，我们就有机会返回`score`的值：

2.返回函数也是完全可以的

```python
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Student Object (name:%s)" % self.name

    def __getattr__(self, item):
        #属性score不存在时
        if item == 'score':
            return 100
        #函数age()不存在时
        if item == 'age':
            return lambda: 25
        
if __name__ == '__main__':
    print(Student('Michael').score)
    print(Student('Michael').age())
```

3.链式调用

```python
class Chain(object):
    #path='' 表示如果实例化类时未给出path的值，则使用path的默认值''
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path
    
    def __call__(self, user_name=''):
        return Chain('%s/%s' % (self._path, user_name))


    __repr__ = __str__

if __name__ == '__main__':
	print(Chain().status.user.timeline.list)
    print(Chain().users('michael').repos)
```

### __call__

任何类，只需要定义一个`__call__()`方法，就可以直接对实例进行调用。

`__call__()`还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象

能被调用的对象就是一个`Callable`对象

通过`callable()`函数，我们就可以判断一个对象是否是“可调用”对象。

```python
class Chain(object):

    # path='' 表示如果实例化类时未给出path的值，则使用path的默认值''
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    # __call__使得类实例可以被当作函数一般来调用
    def __call__(self, user_name=''):
        return Chain('%s/%s' % (self._path, user_name))

    __repr__ = __str__
    
if __name__ == '__main__':
    print(Chain().users('michael').repos)
```



## 枚举类

为这样的枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例

`value`属性则是自动赋给成员的`int`常量，默认从`1`开始计数

`@unique`装饰器可以帮助我们检查保证没有重复值。

```python
from enum import Enum, unique

@unique
class Weekday1(Enum):
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
    Sun = 7
    
Weekday = Enum('Weekday', ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'))

for name, member in Weekday.__members__.items():
    print(name, "=>", member, "=>", member.value)
```

## 元类

### type()

动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的

`type()`函数既可以返回一个对象的类型，又可以创建出新的类型

要创建一个class对象，`type()`函数依次传入3个参数：

1. class的名称；
2. 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
3. class的方法名称与函数绑定，这里我们把函数`fn`绑定到方法名`hello`上。

```python
def fn(self, name="world"):
    print("Hello,%s" % name)


Hello = type('Hello', (object,), dict(hello=fn))
h = Hello()
h.hello()
```

### metaclass

先定义metaclass，就可以创建类，最后创建实例

metaclass允许你创建类或者修改类

# 错误、调试和测试

## 错误处理

`try...except...finally...`

Python的错误其实也是class，所有的错误类型都继承自`BaseException`

常见的错误类型和继承关系看这里：https://docs.python.org/3/library/exceptions.html#exception-hierarchy

```python
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')
```

## 调试

### assert

`assert`断言的意思是，表达式`n != 0`应该是`True`，否则，根据程序运行的逻辑，后面的代码肯定会出错。

启动Python解释器时可以用`-O`参数来关闭`assert`

 	注意：断言的开关“-O”是英文大写字母O，不是数字0。

### logging

记录信息的级别有`debug`，`info`，`warning`，`error`等几个级别，等级依次递增

### pdb

第4种方式是启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态

### pdb.set_trace()

这个方法也是用pdb，但是不需要单步执行，我们只需要`import pdb`，然后，在可能出错的地方放一个`pdb.set_trace()`，就可以设置一个断点

可以用命令`p`查看变量，或者用命令`c`继续运行：

```python
import logging
import pdb

logging.basicConfig(level=logging.INFO)


def foo(s):
    n = int(s)
    # assert n != 0, 'n is zero'
    # logging.info('n = %d' % n)
    pdb.set_trace()
    print('hello')
    print(10 / n)


if __name__ == '__main__':
    pass
    foo('0')
```

## 单元测试

为了编写单元测试，我们需要引入Python自带的`unittest`模块

编写一个测试类，从`unittest.TestCase`继承。

以`test`开头的方法就是测试方法，不以`test`开头的方法不被认为是测试方法，测试的时候不会被执行。

`unittest.TestCase`提供了很多内置的条件判断，我们只需要调用这些方法就可以断言输出是否是我们所期望的

可以在单元测试中编写两个特殊的`setUp()`和`tearDown()`方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。



```python
import unittest


class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except Exception:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


class testDict(unittest.TestCase):
    
    def setUp(self):
        print('测试前...')

    def tearDown(self):
        print('测试后...')
        
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d['key'], 'value')

    def test_attr(self):
        d = Dict()
        d.name = 'Michael'
        self.assertEqual(d.name, 'Michael')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty


if __name__ == '__main__':
    unittest.main()

```

## 文档测试



测试异常的时候，可以用`...`表示中间一大段烦人的输出

```python
def fact(n):
    '''
    >>> fact(1)
    1
    >>> fact(10)
    3628800
    >>> fact(-1)
    Traceback (most recent call last):
        ...
    ValueError
    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    pass
```

# IO编程

## 文件读写

### 读文件

要以读文件的模式打开一个文件对象，使用Python内置的`open()`函数，传入文件名和标示符：

如果文件不存在，`open()`函数就会抛出一个`IOError`的错误，并且给出错误码和详细的信息告诉你文件不存在

如果文件打开成功，接下来，调用`read()`方法可以一次读取文件的全部内容，Python把内容读到内存，用一个`str`对象表示

Python引入了`with`语句来自动帮我们调用`close()`方法

最后一步是调用`close()`方法关闭文件

```python
fpath = r'D:\PycharmProjects\LiaoXueFeng\IO编程\text.txt'

if __name__ == '__main__':
    with open(fpath, 'r') as f:
        s = f.read()
        print(s)
        print(type(s))
```

`read()`会一次性读取文件的全部内容

`readline()`可以每次读取一行内容，

`readlines()`一次读取所有内容并按行返回`list`。

file-like Object:有个`read()`方法的对象

`StringIO`就是在内存中创建的file-like Object，常用作临时缓冲



要读取二进制文件，比如图片、视频等等，用`'rb'`模式

要读取非UTF-8编码的文本文件，需要给`open()`函数传入`encoding`参数

`open()`函数还接收一个`errors`参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：

### 写文件

调用`open()`函数时，传入标识符`'w'`或者`'wb'`表示写文本文件或写二进制文件

可以反复调用`write()`来写入文件，但是务必要调用`f.close()`来关闭文件，当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。只有调用`close()`方法时，操作系统才保证把没有写入的数据全部写入磁盘

写入特定编码的文本文件，请给`open()`函数传入`encoding`参数，将字符串自动转换成指定编码

以`'w'`模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）

`'a'`以追加（append）模式写入

## StringIO和BytesIO

### StringIO

在内存中读写str

要把str写入StringIO,先创建一个StringIO,然后，像文件一样写入即可`getvalue()`方法用于获得写入后的str

要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取

### BytesIO

在内存中读写bytes

```python
from io import StringIO, BytesIO


def WSIO():
    f = StringIO()
    f.write('hello,world!')
    print(f.getvalue())


def RSIO():
    f = StringIO('Hello!\nHi!\nGoodBye!')
    while True:
        s = f.readline()
        if s == '':
            break
        print(s.strip())


def WBIO():
    f = BytesIO()
    f.write("你好".encode('utf-8'))
    print(f.getvalue())


def RBIO():
    f = BytesIO(b'\xe4\xbd\xa0\xe5\xa5\xbd')
    print(f.read().decode(encoding='utf-8'))
```

## 操作文件和目录

```python
import os

if __name__ == '__main__':
    # 操作系统类型
    print(os.name)
    # 所有环境变量
    print(os.environ)
    # 获取某个环境变量的值
    print(os.environ.get('PATH'))
    # 当前绝对路径
    print(os.path.abspath('.'))
    # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
    # print(os.path.join('D:\PycharmProjects\LiaoXueFeng\IO编程', 'testdir'))
    # 然后创建一个目录:
    # print(os.mkdir(r'D:\PycharmProjects\LiaoXueFeng\IO编程\testdir'))
    # 删除一个目录
    # print(os.rmdir(r'D:\PycharmProjects\LiaoXueFeng\IO编程\testdir'))
    # 拆分路径
    print(os.path.split(r'D:\PycharmProjects\LiaoXueFeng\IO编程\testdir'))
    # 获取文件拓展名
    print(os.path.splitext(r'D:\PycharmProjects\LiaoXueFeng\IO编程\SBIO.py')[1])
    # 重命名
    # print(os.rename('test.py', 'test1.py'))
    # 删除文件
    # print(os.remove('test1.py'))
    # shutil模块提供了copyfile()的函数
    # 列出当前目录下所有目录
    print([x for x in os.listdir('.') if os.path.isdir(x)])
    # 列出当前目录下所有.py文件
    print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

    pass

```

## 序列化

在程序运行的过程中，所有的变量都是在内存中

把变量从内存中变成可存储或传输的过程称之为序列化

`pickle`模块可以用来实现序列化



# 进程和线程

## 多进程

## 多线程

1.Threading模块

threading.current_thread()函数永远返回当前线程的实例

Python 有一个GIL(Globle Interpreter Lock)锁，任何Python线程在执行前都会获得GIL锁，每执行100条字节码，解释器就自动释放GIL，所以多线程在Python中只能交替执行。



## 分布式进程

```python
# -*- coding: utf-8 -*-
# TaskMaster.py

# distributed multi process, task manager
from multiprocessing import managers
import random, time, queue
from multiprocessing.managers import BaseManager

# queue that send tasks
task_queue = queue.Queue()
# queue that receive tasks
result_queue = queue.Queue()


class QueueManager(BaseManager):
    pass


def get_task_q():
    return task_queue


def get_result_q():
    return result_queue


if __name__ == '__main__':
    # register two queues to network
    QueueManager.register('get_task_queue', callable=get_task_q)
    QueueManager.register('get_result_queue', callable=get_result_q)
    # bind to port 5000, authentication code abc
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')

    # start the manager
    manager.start()
    # get Queue object through network
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # put some tasks to task queue
    for i in range(10):
        n = random.randint(0, 10000)
        print(f"Put task %d" % n)
        task.put(n)

    # read result from result queue
    print("Try get results...")
    for i in range(10):
        try:
            r = result.get(timeout=5)
            print(f"Result : {r}")
        except queue.Empty:
            print("The queue is empty...")

    manager.shutdown()
    # shudown manager
    print("Master exit.")

```

```python
# -*- coding: utf-8 -*-
# TaskWorker.py

# distributed multi process, task wroker
import time, sys, queue
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


if __name__ == '__main__':
    QueueManager.register('get_task_queue')
    QueueManager.register('get_result_queue')
    server_addr = "127.0.0.1"
    print(f"Connect to server {server_addr}...")
    m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
    # connect to server
    m.connect()
    # get Queue from network
    task = m.get_task_queue()
    result = m.get_result_queue()
    # get task from task queue, calculate and put result to result queue
    for i in range(10):
        try:
            n = task.get(timeout=1)
            print(f"Run task {n} * {n}...")
            r = f"{n} * {n} = {n * n}"
            # time.sleep()是效果更加清楚
            time.sleep(1)
            result.put(r)
        except queue.Empty:
            print("task queue is empty.")

    # end wrok process
    print("Worker exit.")

```


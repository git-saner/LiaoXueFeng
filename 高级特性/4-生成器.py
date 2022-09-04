# -*- coding : utf-8 -*-
# @Time : 2022/9/1 8:30
# @Author : Saner
# @File : 4-生成器.py
# @Software : PyCharm

# a, b = 0, 1
# a, b = b, a + b
# print(a, b)

'''
杨辉三角定义如下：
          1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \
1   5   10  10  5   1
把每一行看做一个list，试写一个generator，不断输出下一行的list
'''

'''
def triangles(max):
    L = [1]
    n = 1
    while n <= max:
        yield L
        temp = L
        n += 1
        # 生成列表生成式
        for x in range(n):
            print("第%d次循环" % (x + 1))
            if x == 0:
                L[x] = temp[x]
                continue
            if x == (n - 1):
                L[x] = temp[x - 1]
                continue
            L[x] = temp[x - 1] + temp[x]


n = 1
tr = triangles(6)
while n <= 6:
    next(tr)
'''

g = (x * x for x in range(10))
for n in g:
    print(n)


def add(x, y, f):
    return f(x) + f(y)


print(add(-5, 6, abs))

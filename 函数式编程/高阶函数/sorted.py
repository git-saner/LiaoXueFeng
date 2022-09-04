# -*- coding : utf-8 -*-
# @Time : 2022/9/4 9:28
# @Author : Saner
# @File : sorted.py
# @Software : PyCharm

l1 = ['bob', 'about', 'Zoo', 'Credit']
l2 = [-21, -12, 5, 9, 36]

print(sorted(l2,key=abs))
print(sorted(l1,key=str.lower))
print(sorted(l1,key=str.lower,reverse=True))

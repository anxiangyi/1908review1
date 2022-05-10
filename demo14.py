'''
python 垃圾回收机制:
1.引用计数为主   缺点：循环引用导致内存泄露

2.标记清除为辅
3.隔代回收为辅
'''
# import sys
#
# name = 'junxiao'
# name1 = name
#
# print(sys.getrefcount(name))
import sys

li1 = [11, 22]

li2 = [22, 33]

li1.append(li2)  # [11,22,[22,33]]
print(sys.getrefcount(li2))

li2.append(li1)
print(sys.getrefcount(li1))

del li1

del li2



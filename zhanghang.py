# import random
#
# list1=range(2,19)
#
# s='abcdef'
# for i in range(-1,-len(s),-1):
#     print(s[:i])
#
# s2 = 'abcde'
# i = -1
# for i in [None] + list(range(-1, -len(s2), -1)):
#     print(s2[:i])
# c=random.random()
# print(c)
#
# from collections import Iterable, Iterator
# s = 'admin'
# s = iter(s)
# print(isinstance(s, Iterator))  # True
#
# #
# g = (i for i in range(1,10))
# print(isinstance(g, Iterator))
# print(isinstance(g, Iterable))
x = ['a', 'b', 'c']
for i, v in enumerate(x):
    print('遍历出来的值的下标是{0},值是{1}'.format(i, v))
mydict={'a':1,'b':2,'c':3,'e':5}
a=mydict.keys()
print(a)
mydict

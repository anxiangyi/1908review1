'''
列表推导式（集合推导式，字典推导式）:
生成器   迭代器   可迭代的
generator  生成器
1. 列表推导的格式
2. 函数+yield  yield关键字：暂停  就是生成器

得到生成器里面的下一个元素： next()  g.__next__()  g.send()
如果取不出来了则报：StopIteration

迭代器: Iterator  Iterable
可迭代的未必是迭代器，可以通过iter()将其转成迭代器
生成器是迭代器的一种。


迭代器、生成器有什么好处？
节省内存
惰性求值

'''
# from collections import Iterable, Iterator
#
# list1 = [12, 5, 8, 14, 7, 0, 6, 12, 8]
# # 获取list1偶数
# # list2 =[]
# # for i in list1:
# #     if i%2==0:
# #         list2.append(i)
# # print(list2)\
#
# list2 = [i for i in list1 if i % 2 == 0]
# print(list2)
#
# # 偶数-5  奇数+2
# list3 = [i - 5 if i % 2 == 0 else i + 2 for i in list1]
# print(list3)
#
# # 集合推导式
# # 获取list1偶数
# set1 = {i for i in list1 if i % 2 == 0}
# print(set1)
#
# # {‘001’:‘aaa’,'002':'bbb'}  ---> {'aaa':'001','bbb':'002'}
# dict0 = {'001': "aaa", '002': 'bbb'}
# dict1 = {v: k for k, v in dict0.items()}
# print(dict1)

# 1-1000  [1,2,3,.....1000]
g = (i for i in range(1, 6))
print(g)

print(next(g))
print(next(g))
print(next(g))
print(next(g))

print(g.__next__())


# print(g.send(None))


# 定义一个生成器实现获取斐波那契数列  1,1,2,3,5,8,13，
def fib(n):
    a, b = 0, 1
    if n == 1 or n == 2:
        yield 1
    if n > 2:
        a, b = b, a + b
        yield b

g1 = fib(5)

print(g1.__next__())


# def fib(max):
#     x, y = 0, 1
#     while y < max:
#         yield y  # 暂停 + return
#         x, y = y, x + y
#
#
# g = fib(5)
#
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# # 可迭代和迭代器
# print(isinstance(5, Iterable))  # False
# print(isinstance('admin', Iterable))  # True
# print(isinstance([1, 2, 3, 4, 5], Iterable))  # True
# # str，list，dict，set，tuple  可迭代的
# # int，float  不可迭代的
#
# print(isinstance('admin', Iterator))  # False
# print(isinstance([1, 2, 3, 4, 5], Iterator))
# # 可迭代的未必是迭代器
# s = 'admin'
# s = iter(s)
# print(isinstance(s, Iterator))  # True
#
#
# g = (i for i in range(1,10))
# print(isinstance(g, Iterator))
# print(isinstance(g, Iterable))
#
#
# class MyIterator(object):
#     def __init__(self, n):
#         self.n = n
#         self.current = 0
#
#     # 自定义迭代器需要重写__iter__和__next__方法
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current < self.n:
#             value = self.current
#             self.current += 1
#             return value
#         else:
#             raise StopIteration
# #
# #
# my_it = MyIterator(10)
# #
# for i in my_it:  # 迭代器重写了__iter__方法，它本身也是一个可迭代对象
#     print(i)

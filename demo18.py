'''
单例模式:
    开发模式
    确保某一个类只有一个实例存在.

'''

# class Person:
#     # 私有化类属性
#     __instance = None  # 保存地址
#
#     def __new__(cls, *args, **kwargs):
#
#         if cls.__instance == None:
#             cls.__instance = object.__new__(cls)
#
#         return cls.__instance
#
#     def __init__(self):
#         print('----->初始化方法')
#
#
# p = Person()
#
# print(p)
#
# p1 = Person()
#
# print(p1)
#
# p2 = Person()
#
# print(p2)

# 封装函数Singleton
from time import sleep


def Singleton(cls):
    _instance = {}  # set1 = set()

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton


@Singleton
class A:
    a = 1

    def __init__(self, x=0):
        self.x = x


@Singleton
class B:
    b = 1

    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y


# a1 = A()
# print(a1)
#
# a2 = A(x=8)
# print(a2)


# 单例类
class Singleton(object):

    def __init__(self):
        sleep(1)

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            Singleton._instance = Singleton(*args, **kwargs)
        return Singleton._instance


#
# for i in range(10):
#     s = Singleton.instance()
#     print(s)

#
import threading


def task(arg):
    obj = Singleton.instance()
    print(obj)


for i in range(10):
    t = threading.Thread(target=task, args=[i, ])
    t.start()

# ----------------------------


import threading


class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance

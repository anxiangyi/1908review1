'''
 == is的区别
  == 比较的是内容
  is 比较的是地址
  自定义对象的== ，is如何使用？
  ==  重写类中__eq__魔术方法： 1. 判断地址 2.判断内容
  is  比较的是地址
'''
__all__ = ['a', 'b']

a = 10
b = 10

print(a == b)  # True
print(a is b)  # True

list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(id(list1), id(list2))
print(list1 == list2)  # True
print(list1 is list2)  # False


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    # 必须重写__eq__方法
    def __eq__(self, other):  # equals
        if self is other:
            return True
        return self.name == other.name


p = Person('张三')
p1 = Person('张三1')
p2 = p1

print(p1 == p)
print(p is p1)
print(p2 is p1)
print(p2 == p1)

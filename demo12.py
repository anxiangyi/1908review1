'''
魔术方法:
  无需调用，在某种场景下自动会执行的方法。

  __str__, __repr__

  共同： 对象的字符串表示形式，当打印对象名会自动调用此魔术方法

  如果两者都重写:
  print(对象名)  ----》 __str__
  print(repr(对象名))  ----》 __repr__

  常用:__str__

  __new__ ,  __init__

  创建对象的时候会被调用。
      __new__（表示开辟空间）
      __init__ (初始对象空间)

  __eq__  __gt__  __lt__


  __call__  __del__


'''


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "哈哈哈"

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if self is other:
            return True
        else:
            if self.name == other.name and self.age == other.age:
                return True
            return False

    def __gt__(self, other):
        return self.age > other.age

    def __lt__(self, other):
        return self.age < other.age

    def __call__(self, *args, **kwargs):
        print('-------->call')
        for i in args:
            print(i)
        print(kwargs)

    def __del__(self):
        print('-------->del')


p1 = Person('帅阳', 20)
p2 = Person('帅阳', 22)

print(p1)

# 调用对象 （把对象当成函数一样使用）
p1(11, 2, 23, 4, name='abc')

p1(n=1, m=2)

# print(p1 == p2)
# print(p1 is p2)
#
# # 只要两个对象比较则比较的是年龄
# print(p1 > p2)
#
# print(p1 < p2)

# print(p)
# print(repr(p))
# print(p.__str__())
# print(p.__repr__())

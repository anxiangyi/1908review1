'''
  重写  重载(鸭子模型)

  重写：
  重载： 方法名字相同，参数的个数，类型，顺序 则认为构成重载。

'''


class Person:
    def run(self):
        print('---->person run')


class Student(Person):
    # 子类重写父类的run方法
    def run(self):
        super().run()
        print('-------->student run')

    # def run(self,name,age):
    #     print('------>重载方法')
    #
    # def run(self, age, name):
    #     print('------>重载方法')


s = Student()
s.run()


class X:
    def show(self):
        print('xxxxxx')

    def eat(self):
        print('---->eat')


class Y:
    def show(self):
        print('YYYYYY')

    def sleep(self):
        print('---->sleep')


# 旧式类
# class Animal:
#     pass

# 新式类
class Animal(X, Y):
    pass


a = Animal()
a.show()
a.eat()
a.sleep()

print(Animal.__mro__)

# max = 30


def outer():
    # max = 20

    def inner():
        # max = 10
        print(max)

    inner()

outer()


z=zip(('a','b','c','d','e'),(1,2,3,4,5))

z1 =list(z)
print(dict(z))

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
print(A0)
A1 = range(10)
A2 = [i for i in A1 if i in A0]
A3 = [A0[s] for s in A0]
A4 = [i for i in A1 if i in A3]

print(A1)
print(A2)
print(A3)
print(A4)
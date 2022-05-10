'''
metaclass 元类
 对象是类的实例，类本身也是一个对象(实例)，是type的实例
 Person类就是type构建的实例

 type本身又是type类的实例   type称作元类（metaclass）

'''

print(type(int))
print(type(str))
print(type(list))
print(type(dict))

a = 10


class Mymetaclass(type):
    print(123456)
    def __new__(cls, *args, **kwargs):
        print('---->metaclass __new__')
        return type.__new__(cls, *args, **kwargs)


print('--------->1')


class Person(metaclass=Mymetaclass):
    # __metaclass__ = Mymetaclass

    def __init__(self):
        print('-------->person __init__')


print('------------>2')

p = Person()

print('------------>3')

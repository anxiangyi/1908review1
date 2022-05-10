class Person:
    def __init__(self, name, age):
        # 私有化
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def __str__(self):
        return self.__name + '---' + str(self.__age)


p = Person('张三', 19)

print(p.name)

p.name = '李四'

print(p)

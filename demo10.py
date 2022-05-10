class Person(object):
    type = '人类'
    def __new__(cls, *args, **kwargs):
        print('----->new')
        return object.__new__(cls)   # 让内存开辟空间

    def __init__(self, name):  # 返回值赋值给self  就是内存空间
        print('----->init')
        self.name = name  # 向self这个内存空间添加属性name

    def run(self):
        print('------>run')

    @classmethod
    def show1(cls):
        print('------》classmethod')

    @staticmethod
    def show2():
        print(Person.type)
        print('无法获取对象的内容')
        print('------>staticmethod')


# self  如何理解当前self
# p = Person('aaa')
#
# p.run()  # 对象本身

Person.show1()

Person.show2()

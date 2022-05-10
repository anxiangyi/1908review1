class Person:
    # 限制类的动态属性添加
    # __slots__ = ['a', 'b']

    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
        self.__d= 40

    # def __str__(self):
    #     return self.a


p = Person()
# p.x = 100  通过__slots__ 限制只能用a，b
# p.a = 100
print(p)

print(p.__dict__)  # 查看当前对象的属性并以字典方式返回

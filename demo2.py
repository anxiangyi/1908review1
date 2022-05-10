'''
闭包和装饰器：
闭包：
1. 一个函数中嵌套了另一个函数
2. 内部函数引用了外部函数的变量
3. 返回值是内部函数


装饰器:
装饰器可以完成：
1. 登录验证
2. 权限验证
3. 日志记录
4. 计数器

'''


def outter(m):
    name = 'hello'

    def inner():
        nonlocal m
        m += 1
        return m

    return inner


def decorator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print('刷墙')
        print('铺地板')

    return wrapper


@decorator
def house(area):
    print('我是{}平的毛坯房'.format(area))


house(100)
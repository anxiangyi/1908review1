'''
三层装饰器
'''


def decorator(name):
    def wrapper1(func):
        def wrapper2(*args, **kwargs):
            func(*args, **kwargs)
            print('正在装修房子的：{}'.format(name))
            return 'OK'

        return wrapper2

    return wrapper1


@decorator('卧室')
def house():
    print('我是毛坯房....')


if __name__ == '__main__':
    house()
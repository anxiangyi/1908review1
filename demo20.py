'''
文件操作：
 open()  ----> 本地文件的IO操作

 stream = open('绝对|相对')   ----> 默认是“读文本流”
  r read  w write  a append

  t text   b  binary

  stream = open('路径'，‘w+’)

  stream.read()
  stream.write()

  stream.close()

  with open(...) as xxx:
     ....

with表达式其实是try-finally的简写形式。但是又不是全相同。
with关键字：流操作自动执行关闭操作
try：
   。。。。
finally:
  stream.close()

try...except
try...finally
try....except...else
try....except...else....finally

'''


class Mycontex(object):
    def __init__(self, name):
        self.name = name
        print('-------init')
    #
    # def __enter__(self):
    #     print("进入enter")
    #     return self

    def do_self(self):
        print(self.name)
        raise NameError('命名有误！')

    # def __exit__(self, exc_type, exc_value, traceback):
    #     print("退出exit")
    #     print(exc_type, exc_value)


if __name__ == '__main__':
    with Mycontex('test') as mc:
        mc.do_self()
        print('------>context')


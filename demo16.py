'''
协程:
  gevent----> greenlet
  猴子补丁
'''

import time
import gevent
from gevent import monkey

# 猴子补丁

monkey.patch_all()


def eat():
    for i in range(5):
        print('正在吃第{}个馒头'.format(i + 1))
        time.sleep(0.6)  # 自动切换


def listen():
    for i in range(5):
        print('正在听第{}首歌'.format(i + 1))
        time.sleep(0.6)


if __name__ == '__main__':
    g1 = gevent.spawn(eat)
    g2 = gevent.spawn(listen)

    g1.join()
    g2.join()

    print('-----over-----')

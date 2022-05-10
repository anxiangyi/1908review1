'''
线程共享数据
GIL

'''
import threading
from time import sleep

number = 0


def task():
    global number
    lock.acquire()  # 拿到锁
    for i in range(1000000):
        number += 1
        # sleep(0.1)
    lock.release()  # 释放锁
    print('{}----->number:{}'.format(threading.current_thread().name, number))


if __name__ == '__main__':
    lock = threading.Lock()
    t1 = threading.Thread(target=task, name='AAAAA')
    t2 = threading.Thread(target=task, name='BBBBB')

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print('----->main:', number)

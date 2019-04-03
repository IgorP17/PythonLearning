import multiprocessing
import time
import os


def f(name):
    print('hello', name)

if __name__ == '__main__':
    p = multiprocessing.Process(target=f, args=('bob',))
    p.start()
    p.join()
    p = multiprocessing.Process(target=f, args=('ann',))
    p.start()
    p.join()
# coding: utf-8
""" gpool里所有 的greenlet执行完毕，是否会删除gpool？
结论 不会
实现思路：
    gpool里丢2个任务。
    join完事以后
    再丢1个试试看看会不会继续运行。
运行结果：
***res***
i was sleep 1 sec
i was sleep 1 sec
1522371885.5
1522371885.5
----end---?
0 [当前gpool  len]
----in---add----
6 [下一个任务的输出]
****res****
"""

from gevent import monkey; monkey.patch_all()
from gevent.pool import Pool as gpool
import requests
import time


def delay_func():
    time.sleep(1)
    print('i was sleep 1 sec')


def add(x, y):
    print('----in---add----')
    print(x+y)


def main():
    for i in range(2):
        gpool.apply(delay_func)
    print(time.time())
    gpool.join()
    print(time.time())
    print('----end---?')
    print(len(gpool))
    gpool.apply_async(add, args=[4,2])
    gpool.join()


if __name__ == '__main__':
    main()
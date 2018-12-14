# coding: utf-8
from multiprocessing import Process
import os, time
import sys


def lazy_func():
    print('my credit id is {}, start to sleep 10*2 '.format(os.getpid()))
    time.sleep(10 * 2)
    print ('do do do something,{}'.format(os.getpid()))


def test_simple_parallel():
    start_time = time.time()
    p_list = []
    for i in range(5):
        p_list.append(Process(target=lazy_func))

    for i in p_list:
        i.start()

    for i in p_list:
        i.join()

    end_time = time.time()
    print ('total time dealta {}'.format(end_time-start_time))  # total time dealta 20.0086579323

    """
    lazy_func 日志交替输出。
    主进程顺序输出。
    total dealta time 约等于 执行一次lazy_func的时间
    """
# todo : multiprocess 操作数据库。
# todo: gevent+pymysql 操作数据库。高并发写数据库。数据库conn什么时候初始化。cursor是不是用一次关一次。读写同一列会不会有问题。卡住的情况是为什么/

test_simple_parallel()
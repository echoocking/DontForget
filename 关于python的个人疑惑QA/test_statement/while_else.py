# coding: utf-8
import random


class WhileElse(object):

    def run(self):
        """
        结果：
        apply error, e is
        apply error, e is
        else里的东西while没有被内部中断 就可以执行

        """
        api_retry = 0
        retry_times = 1
        while api_retry <= retry_times:
            try:
                raise ValueError
                break
            except Exception, e:
                print('apply error, e is {}'.format(e))
                api_retry += 1
        else:
            print 'else里的东西while没有被内部中断 就可以执行'

    def run_my_statement(self):
        """
        改进run
        我想实现的是 当重试失败之后直接return None
        """
        api_retry = 0
        retry_times = 1
        while api_retry <= retry_times:
            try:
                cheat = random.choice([0, 1])
                if not cheat:
                    print 'not cheat'
                    raise ValueError
                print 'cheat'
                break
            except Exception, e:
                print('apply error, e is {}'.format(e))
                api_retry += 1
        if api_retry > retry_times:
            return
        else:
            print '千山万水总是情， 不吃香菜行不行'

WhileElse().run_my_statement()
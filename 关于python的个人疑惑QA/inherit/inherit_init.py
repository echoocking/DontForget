# coding: utf-8
"""
测试继承初始化
"""


class Pa(object):
    def __init__(self):
        self.name = 'papa'
        self.water = 'ice_tea'

    def get_drink(self):
        return self.water


class P1(Pa):

    def __init__(self):
        super(P1, self).__init__()
        self.wife = 'mary'

    def hug(self):
        print self.name
        print 'hug : {}'.format(self.wife)


# print 'import test'  # for test_import


def test_init_and_new():
    """
    遇到一种有毒的写法。为了不让直接实例化，把__init__方法干掉了。
    :return:
    """
    someone1 = P1()
    P1.__init__ = None  # someone2 报错：TypeError: 'NoneType' object is not callable
    # P1.__new__ = None  # someone2 报错：TypeError: 'NoneType' object is not callable
    someone2 = P1()


class Singleton(object):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        print '我在new里，你在哪里？'
        return cls._instance

    """
    为什么要传入cls, *args, **kwargs。因为要实例化这个类变量阿哥。然后需要把传入的参数绑定到实例上。
    所以测试一下类方法是不是不会调用__new__。
    """

    @classmethod
    def class_func(cls):
        print '我是一个米有感情的杀手'

    @staticmethod
    def static_func():
        print '我是一个静态的小口爱'

    def instance_func(self):
        print '我是一个什么都不写的家伙'


if __name__ == '__main__':
    Singleton.class_func()  # res:  我是一个米有感情的杀手
    Singleton().class_func()  # 我在new里，你在哪里？  我是一个米有感情的杀手
    print '-----------'
    Singleton.static_func()  # 我是一个静态的小口爱
    print '----------'
    Singleton().static_func()  # 我在new里，你在哪里？ 我是一个静态的小口爱
    print '----------'
    Singleton().instance_func()
    print '---final ----shot---'
    Singleton.instance_func()  # 看吧 pylint都会报错yo～

"""
结论 
1. 不实例化 是不会调用__new__的哦
2. 静态方法可以被类/类实例调用【2.7】
3. 类方法可以被类/类实例调用【2.7】
4. 实例方法只能被实例调用 TypeError: unbound method instance_func() 

"""

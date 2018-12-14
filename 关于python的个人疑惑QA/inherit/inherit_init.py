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
    """ 实现单例模式 """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        print '我在new里，你在哪里？'
        return cls._instance

    """
    为什么要传入cls, *args, **kwargs。因为要实例化这个类。然后需要把传入的参数绑定到实例上。
    所以测试一下类方法是不是不会调用__new__。
    """

    @classmethod
    def class_func(cls):
        print '我是一个米有感情的杀手'

    @staticmethod
    def static_func():
        print '我是一个静态的小口爱'  # 静态方法什么都不需要传入。所以既不可以访问类变量，也不可以访问实例变量，真单纯不做作，23333

    def instance_func(self):
        """可以访问类变量，也可以访问实例变量。因为python在实例话的时候，会把类变量deepcopy一份给每一个实例。
        相当于把所有类变量都给自动转了成为实例变量。所以直接修改类变量是不行的哟，而且你也没有cls。
        想要修改类变量还是老老实实去类方法里改吧"""
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
5. 在实行 Singleton()的时候，就会调用__init__ 方法。所以在继承父类初始化的时候，不要Singleton().__init__()这么写。这样写会两次
调用__init() 方法。有时候粗心会没有注意。Singleton.__init__()，这样写是ok的。另外多重继承的时候

"""


# 经典类
class A():
    def __init__(self):
        print 'A'


class B(A):
    def __init__(self):
        A.__init__(self)
        print 'B'


class C(B, A):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print 'C'

"""
使用经典继承里，不要这么写。B继承于A，C继承于A和B, 但C需要调用父类的init()函数时，
前者会导致父类A的init()函数被调用2次，这是不希望看到的。而且子类要显式地指定父类，不符合DRY原则
"""

# 新式类


class A(object):
    def __init__(self):
        print 'A'


class B(A):
    def __init__(self):
        super(B, self).__init__()
        print 'B'


class C(B, A):
    def __init__(self):
        super(C, self).__init__()
        print 'C'


"""
采用super()方式时，会自动找到第一个多继承中的第一个父类，但是如果还想强制调用其他父类的init()函数或两个父类的同名函数时，就要用老办法了。
"""
"""
2018年01月11日21:37:13
再听 尾崎豊 的 I LOVE YOU 的夜晚
北京 学院路街道
"""

"""
第一种写法 lambda定义了一个匿名函数，其未传入参数。函数执行时，结合列表生成式，生成[i, i, i]的结构
最后一轮迭代完成后，i=2，故输出为 2，2，2
"""

f1, f2, f3 = [lambda: i for i in range(3)]
print(f1, f2, f3)
print(f1(), f2(), f3())

"""
第二种写法i通过传入参数的方式将i的值赋值给参数num，参数自己会开辟内存空间，故其值不收i的变化所影响
输出为1，4，9
"""


def get_multi(num):
    def inner():
        return num*num
    return inner

f4, f5, f6 = [get_multi(i) for i in range(1, 4)]
print(f4(), f5(), f6())


""""
第三中类似于第一种，fs内部绑定了i，i本应该被随着count的调用结束而被销毁，但由于f内还存在i的引用
故i未被销毁，但是i也只有一处内存空间，故输出为9，9，9
"""


def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

"""
当函数存在嵌套，并且子函数引用了父函数中的变量，可以访问这些变量的作用域就形成闭包。2 如果子函数没有访问父函数中的变量，就不存在闭包。
"""

# lambda 如何传入参数呀？
lres = [i for i in map(lambda x: x*x, range(3))]
print(lres)
# [0, 1, 4]


# 装饰器的编写呢
"""
装饰器作用为 增强函数功能
"""


def wapper_func(func, *args, **kwargs):
    if args:
        print('我有参数啦')

    def inner_func(func):
        return func(args, kwargs)
    return inner_func

# @wapper_func

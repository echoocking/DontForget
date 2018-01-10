class Parent(object):
    x = 1


class ChildrenA(Parent):
    pass


class ChildrenB(Parent):
    pass

print(Parent.x, ChildrenA.x, ChildrenB.x)
ChildrenA.x = 2
print(Parent.x, ChildrenA.x, ChildrenB.x)
Parent.x = 3
print(Parent.x, ChildrenA.x, ChildrenB.x)
ChildrenB.x = 4
print(Parent.x, ChildrenA.x, ChildrenB.x)
Parent.x = 5
print(Parent.x, ChildrenA.x, ChildrenB.x)
"""
这里是对于继承中变量的理解:
父类修改自己的类变量时，当子类未修改对应的类变量，那么可以看做子类中的变量是指向父类中的类变量的，子类中的变量也会被修改
父类修改自己的类变量时，子类已经对于此变量进行赋值操作后，子类变量与父类变量相互独立，无影响
子类之间变量修改互不影响

结果如下：
1 1 1
1 2 1
3 2 3
3 2 4
5 2 4
"""
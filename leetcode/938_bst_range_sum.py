# coding: utf-8


class Node:

    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None


class BST:

    def insert(self):
        """
        二叉树的规则是 小于当前节点的值放在左子树，大于当前节点的值放在右子树。所以插入的时候先要查找。
        如果这个值小于节点值，就转左，大于节点值就转右。如果这时 节点对应方向的子节点为空(叶子节点)，就创建新节点，把值插入进去。结束。
        如果对应的子节点不为空，那就再继续进行查找，直到有对应的子节点为空为止。
        :return:
        """
        pass

    def delete(self):
        """
        先进行查找，找到以后进行删除。
        删除好像需要考虑的更多呢
        :return:
        """
        pass

    def search(self, value):
        """
        小于转左，大于转右，直到相等或者下一个对应方向为空。
        好像还有几种遍历方式哦
        :param value:
        :return:
        """
        pass



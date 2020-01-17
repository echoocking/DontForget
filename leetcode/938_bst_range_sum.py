# coding: utf-8


class Node:

    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None


class BST:

    def __init__(self, root_value=None):
        self.root = root_value

    def insert(self, value):
        """
        二叉树的规则是 小于当前节点的值放在左子树，大于当前节点的值放在右子树。所以插入的时候先要查找。
        如果这个值小于节点值，就转左，大于节点值就转右。如果这时 节点对应方向的子节点为空(叶子节点)，就创建新节点，把值插入进去。结束。
        如果对应的子节点不为空，那就再继续进行查找，直到有对应的子节点为空为止。
        :return:
        """
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, node):
        if value > node.value:
            if node.right_node is None:
                node.right_node = Node(value)
                return True
            else:
                self._insert(value, node.right_node)

        elif value < node.value:
            if node.left_node is None:
                node.left_node = Node(value)
                return True
            else:
                self._insert(value, node.left_node)

    def delete(self):
        """
        先进行查找，找到以后进行删除。
        删除好像需要考虑的更多呢
        :return:
        """
        pass

    def search(self, value):
        return self._search(value, self.root)

    def _search(self, value, node):
        """
        小于转左，大于转右，直到相等或者下一个对应方向为空。
        好像还有几种遍历方式哦
        递归写 挺直观的
        :param value:
        :return:
        """

        if node is None:
            return False

        else:
            if value == node.value:
                return True

            if value > node.value:
                self._search(value, node.right_node)
            else:
                self._search(value, node.left_node)

    def front_walk(self):
        self._front_walk(self.root)

    def _front_walk(self, node):
        if node is None:
            return
        print(node.value)
        self._front_walk(node.left_node)
        self._front_walk(node.right_node)

    def _walk(self, node, res: list):
        pass

    def back_walk(self):
        self._back_walk(self.root)

    def _back_walk(self, node):
        if node is None:
            return
        self._back_walk(node.left_node)
        self._back_walk(node.right_node)
        print(node.value)

    def test_walk(self):

        root = Node(4)
        root.left_node = Node(2)
        root.right_node = Node(5)
        root.left_node.left_node = Node(1)
        root.left_node.right_node = Node(3)
        root.right_node.right_node = Node(6)
        root.right_node.right_node.right_node = Node(7)

        tree = BST(root)
        # tree.front_walk()
        tree.back_walk()

        #max, min, order sequence,
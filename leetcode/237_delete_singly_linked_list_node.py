# coding: utf-8

# 删除单链表中的一个节点。
# 这也是链表删除数据非常方便的一个例子
# 删除数据 1. 前后剪断，重新连接 2.后数前移，绕过删除数。 题目挺有意思

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
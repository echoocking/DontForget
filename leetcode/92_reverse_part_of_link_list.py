# coding: utf-8
import copy

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_between(self, head: ListNode, left: int, right: int) -> ListNode:
        """
        循环到left-1的位置，记下来为before
        翻转，俩俩交换，用after记下后面的联系方式
        cur 与cur.next 翻转。after，同时判断是否到了right。

        :param head:
        :param left:
        :param right:
        :return:
        """
        # 走left-1步。
        dummy = ListNode(-100000)
        dummy.next = head

        # 要走的指针取个名字
        pre = dummy
        for i in range(left-1):
            pre = pre.next

        rn = pre.next
        rvsed_tail = pre.next
        ln = pre.next
        pre.next = None
        for _ in range(right - left):
            ln = ln.next

        after = ln.next
        ln.next = None

        rvsed_head = self._reverse_link_list(rn)
        pre.next = rvsed_head
        rvsed_tail.next = after

        return dummy.next

    def _reverse_link_list(self, head: ListNode) -> ListNode:
        """

        :param head:
        :return:
        """
        # if not head.next or not head:  #退出条件：只有一个节点或者是空表， 直接返回
        #     return head
        # # 提取重复逻辑：
        # tmp = head.next
        # head.next = pre
        # self._reverse_link_list(tmp, head)

        if not head.next or not head:
            return head

        final_node = self._reverse_link_list(head.next)  # 走到最后
        head.next.next = head  # 对最后的一个节点进行处理
        head.next = None
        return final_node

    def test(self):
        nn1 = ListNode(1)

        nn2 = ListNode(2)
        nn3 = ListNode(3)
        nn4 = ListNode(4)

        nn5 = ListNode(5)
        nn6 = ListNode(6)

        nn1.next = nn2
        nn2.next = nn3
        nn3.next = nn4
        nn4.next = nn5
        nn5.next = nn6

        res = self.reverse_between(nn1, 2, 4)
        while res:
            print(res.val)
            res = res.next

Solution().test()






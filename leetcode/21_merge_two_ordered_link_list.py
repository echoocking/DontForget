# coding: utf-8
# 合并俩有序链表

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 静态方法不需要实例化也可以使用？

    def merge(self, list1: ListNode, list2: ListNode)->ListNode or None:
        if not list1 and not list2:
            return

        if not list1:

            return list2
        if not list2:

            return list1

        if list1.val <= list2.val:
            r = list1
            list1 = list1.next
        else:
            r = list2
            list2 = list2.next

        return self._merge(list1, list2, r)

    def _merge(self, h1: ListNode, h2: ListNode, r: ListNode)->ListNode:
        if not h1 and not h2:
            return r

        if not h1:
            r.next = h2
            return r
        if not h2:
            r.next = h1
            return r

        if h1.val >= h2.val:
            smaller = h2
            next_h2 = h2.next
            next_h1 = h1
        else:
            smaller = h1
            next_h1 = h1.next
            next_h2 = h2

        r.next = smaller  #选到更小的一个 挂在r后面

        self._merge(next_h1, next_h2, smaller)
        return r

    def test(self):
        n1 = ListNode(1)
        n2 = ListNode(4)
        n3 = ListNode(7)
        n1.next = n2
        n2.next = n3

        nn1 = ListNode(2)
        nn2 = ListNode(3)
        nn3 = ListNode(10)
        nn4  = ListNode(100)
        nn1.next = nn2
        nn2.next = nn3
        nn3.next = nn4

        res = self.merge(n1, nn1)
        while res:
            print(res.val)
            res = res.next

Solution().test()
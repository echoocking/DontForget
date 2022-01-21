# coding: utf-8
# 删除升序链表里重复的元素

# Definition for singly-linked list.

# noNetWork is better


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def remove(self, head) -> ListNode or None:

        all_num = []
        dup_num = []
        fk_header = ListNode(-10000)

        while head:
            if head.val in all_num and head.val not in dup_num:
                dup_num.append(head.val)
            all_num.append(head.val)
            head = head.next

        if all_num:
            head = fk_header
            for i in all_num:
                if i not in dup_num:
                    head.next = ListNode(i)
                    head = head.next
            return fk_header.next

        return None

    def fail_result(self, head) -> ListNode or None:
        """
        失败的理由。
        试图控制的变量太多了
        :param head:
        :return:
        """


    def test(self):

        """
            写的过程中如何准确的高效的调试逻辑？
            按照含义去写
            全面考虑？？
        """

        n1 = ListNode(1)


        res = self.remove(n1)

        while(res):
            print(res.val)
            res = res.next

Solution().test()
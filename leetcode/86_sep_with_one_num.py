# coding: utf-8

"""
分割链表

先查询一个数是否存在？
1.是否要挪，如何挪
大于的用big_head 串起来
小于等于的保留原位置
到最后再把大于的接回去
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        """
        好像理解错了题目意思... 题意：在位置x
        :param head:
        :param x:
        :return:
        """
        dummy = ListNode(next=head)
        h = dummy

        tem = ListNode()
        t = tem

        while dummy.next:
            if dummy.next.val >= x:
                tem.next = ListNode(dummy.next.val)
                tem = tem.next
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next

        else:
            dummy.next = t.next
            return h.next

    def partition_1(self, head: ListNode, x: int) -> ListNode:
        """
        复杂操作直接用俩俩表就行，不用切来切去
        :param head:
        :param x:
        :return:
        """
        fk_head = ListNode(-1000000)
        fk_head.next = head
        cur = fk_head
        bigger_nums_head = ListNode(-1000000)
        bh = bigger_nums_head

        while cur and cur.next:
            if cur.next.val >= x:  # 直到遇到小于等于x的cur指针才可以移动

                while cur.next and cur.next.val >= x:
                    bh.next = cur.next   #大的用新头剪接上 tail赋值None
                    cur.next = cur.next.next  # cur 往后指

                    bh.next.next = None
                    bh = bh.next  # 移动新头指针
                if cur.next:  # 如果cur是最后一个就不移动了，保留最后一个节点
                    cur = cur.next  # 移动cur指针

            else:
                if cur.next:  # 如果cur是最后一个就不移动了，保留最后一个节点
                    cur = cur.next  # 否则移动指针

        if bigger_nums_head.next:
            cur.next = bigger_nums_head.next

        return fk_head.next


    def test(self):

        nn1 = ListNode(1)
        nn2 = ListNode(4)
        nn3 = ListNode(3)
        nn4 = ListNode(2)
        nn5 = ListNode(5)
        nn6 = ListNode(2)

        nn1.next = nn2
        nn2.next = nn3
        nn3.next = nn4
        nn4.next = nn5
        nn5.next = nn6

        res = self.partition_1(nn1, 3)
        while res:
            print(res.val)
            res = res.next

Solution().test()
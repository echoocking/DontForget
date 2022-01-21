# coding: utf-8

# 删除重复元素，使每个元素出现一次
"""
cur.next与cur.next.next比，如果相等，cur.next.next
初始条件 初始时判断，衍生条件的存在性，衍生时判断

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def delete_duplicates(self, head: ListNode) -> ListNode:

        fk_header = ListNode(-100000)
        fk_header.next = head
        cur = fk_header

        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                while cur.next.next and cur.next.next.val == cur.next.val:
                    cur.next.next = cur.next.next.next
            else:
                cur = cur.next
        return fk_header.next

    def test(self):
        nn1 = ListNode(1)
        nn2 = ListNode(1)
        nn3 = ListNode(1)
        # nn4 = ListNode(100)
        nn1.next = nn2
        nn2.next = nn3
        # nn3.next = nn4

        res = self.delete_duplicates(nn1)
        while res:
            print(res.val)
            res = res.next



Solution().test()



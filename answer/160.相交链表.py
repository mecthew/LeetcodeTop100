from typing import List
# Easy

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 链表常用方法：双/快慢指针，虚拟头结点
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        cur1, cur2 = headA, headB
        first_end1, first_end2 = False, False

        while cur1 and cur2:
            if cur1 == cur2:
                return cur1

            cur1 = cur1.next
            cur2 = cur2.next
            if cur1 is None and first_end1 is False:
                first_end1 = True
                cur1 = headB
            if cur2 is None and first_end2 is False:
                first_end2 = True
                cur2 = headA

        return None
from typing import List

# Easy
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None or l2 is None:
            return l1 if l1 else l2

        head = None
        new_list = None
        cur1, cur2 = l1, l2

        while cur1 and cur2:
            if cur1.val < cur2.val:
                node = cur1
                cur1 = cur1.next
            else:
                node = cur2
                cur2 = cur2.next
            if new_list:
                new_list.next = node
                new_list = node
            else:
                new_list = node

            if head is None:
                head = new_list

        rest_l = cur1 if cur1 else cur2
        new_list.next = rest_l
        return head
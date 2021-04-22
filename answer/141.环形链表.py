from typing import List
# Easy
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        fast_p, low_p = head, head
        while fast_p and fast_p.next:
            low_p = low_p.next
            fast_p = fast_p.next.next
            if low_p == fast_p:
                return True
        return False
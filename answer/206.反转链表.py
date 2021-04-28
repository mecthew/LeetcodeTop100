from typing import List

# Easy
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dummy_node = ListNode(next=head)
        prev, cur = None, head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
            if cur:
                dummy_node.next = cur
        return dummy_node.next

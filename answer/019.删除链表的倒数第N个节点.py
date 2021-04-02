from typing import List
# Medium

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy_node = ListNode(next=head)
        prev = dummy_node
        cur = dummy_node

        while n and prev.next:
            prev = prev.next
            n -= 1

        while prev.next:
            cur = cur.next
            prev = prev.next

        if cur:
            tmp = cur.next
            cur.next = cur.next.next
            del tmp
        return dummy_node.next



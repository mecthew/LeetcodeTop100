from typing import List
# Medium

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break

        if fast is None or fast.next is None:
            return None
        else:
            slow2 = head
            while slow != slow2:
                slow = slow.next
                slow2 = slow2.next

            return slow

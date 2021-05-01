from typing import List
# Easy
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# O(1)空间复杂度需要先翻转后半部分链表，再还原
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        def reverse_list(prev_node, cur_node):
            last_node = None
            while cur_node:
                cur_next = cur_node.next
                cur_node.next = last_node
                last_node = cur_node
                prev_node.next = cur_node
                cur_node = cur_next

        mid = slow
        reverse_list(mid, mid.next)
        cur1, cur2 = head, mid.next
        flag = True
        while cur2:
            if cur1.val != cur2.val:
                flag = False
                break
            cur1 = cur1.next
            cur2 = cur2.next
        reverse_list(mid, mid.next)
        return flag


sol = Solution()
a = ListNode(1)
b = ListNode(2)
c = ListNode(2)
d = ListNode(1)
a.next = b
b.next = c
c.next = d
print(sol.isPalindrome(a))
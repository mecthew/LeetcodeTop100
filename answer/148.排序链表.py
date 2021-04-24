from typing import List
# Medium, time O(nlogn), space O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def list_qsort(start, end):
            if start != end:
                cur = start.next
                prev_p = None
                p = start
                while cur != end.next:
                    if cur.val < start.val:
                        cur.val, p.next.val = p.next.val, cur.val
                        prev_p = p
                        p = p.next
                    cur = cur.next
                start.val, p.val = p.val, start.val
                if prev_p:
                    list_qsort(start, prev_p)
                if p != end:
                    list_qsort(p.next, end)

        def merge_sort(head_node):
            if head_node is None or head_node.next is None:
                return head_node

            slow, fast = head_node, head_node.next
            while fast and fast.next:
                slow, fast = slow.next, fast.next.next

            mid, slow.next = slow.next, None
            left, right = merge_sort(head_node), merge_sort(mid)
            h = res = ListNode(0)
            while left and right:
                if left.val < right.val: h.next, left = left, left.next
                else: h.next, right = right, right.next
                h = h.next
            h.next = left if left else right
            return res.next

        h = merge_sort(head)

        return h


sol = Solution()
n1 = ListNode(4)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(1)
n1.next = n2
n2.next = n3
n3.next = n4
ret = sol.sortList(n1)
while ret:
    print(ret.val)
    ret = ret.next
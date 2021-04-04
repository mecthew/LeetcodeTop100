from typing import List
import heapq
# Hard

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        init_heap = [(node.val, ith) for ith, node in enumerate(lists) if node]
        idx2node = {ith: node for ith, node in enumerate(lists) if node}
        heapq.heapify(init_heap)

        head = None
        cur = None
        while init_heap:
            min_val, node_idx = heapq.heappop(init_heap)
            node = idx2node[node_idx]
            if node.next:
                heapq.heappush(init_heap, (node.next.val, node_idx))
                idx2node[node_idx] = node.next

            if cur:
                cur.next = node
            cur = node
            if not head:
                head = cur
        return head


x = list(range(5))
heapq.heapify(x)
print(x)
a = heapq.heappop(x)
print(a, x)
heapq.heappush(x, 0)
print(x)

from typing import List
import heapq
import sys
# Medium
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [num for num in nums[:k]]
        heapq.heapify(max_heap)

        for num in nums[k:]:
            heapq.heappushpop(max_heap, num)
        # print(max_heap)
        ret = heapq.heappushpop(max_heap, sys.maxsize)
        return ret

sol = Solution()
nums = [3,2,1,5,6,4]; k = 2
print(sol.findKthLargest(nums, k))

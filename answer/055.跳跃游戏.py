from typing import List
# Medium

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        furthest_idx = 0

        for ith, num in enumerate(nums):
            if furthest_idx < ith:
                return False

            furthest_idx = max(furthest_idx, ith+num)
            if furthest_idx >= N-1:
                return True

        return furthest_idx >= N-1

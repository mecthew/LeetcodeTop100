from typing import List
import sys

# Easy
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_prev = -sys.maxsize
        max_val = -sys.maxsize

        for num in nums:
            max_prev = max_prev + num if max_prev > 0 else num
            max_val = max(max_val, max_prev)
        return max_val
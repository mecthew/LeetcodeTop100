from typing import List
# Medium

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        p = [0] * (n + 1)
        reversed_p = [0] * (n + 1)
        for i in range(len(nums)):
            p[i+1] = nums[i] * (p[i] or 1)
            reversed_p[n - i - 1] = nums[i] * (reversed_p[n - i] or 1)

        return max(p + reversed_p)


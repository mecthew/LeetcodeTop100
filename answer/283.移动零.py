from typing import List
# Easy

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0
        for ith, num in enumerate(nums):
            if num:
                nums[idx], nums[ith] = num, nums[idx]
                idx += 1

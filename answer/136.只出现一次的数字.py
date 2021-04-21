from typing import List
# Easy

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor_sum = 0
        for num in nums:
            xor_sum ^= num
        return xor_sum

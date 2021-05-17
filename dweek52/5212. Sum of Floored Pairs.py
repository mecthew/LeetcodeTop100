# -*-coding:utf-8-*-
"""
Given an integer array nums, return the sum of floor(nums[i] / nums[j])
for all pairs of indices 0 <= i, j < nums.length in the array. Since the answer
may be too large, return it modulo 109 + 7.

The floor() function returns the integer part of the division.

"""
# Hard, 时间复杂度为O(N + ClogC), C为数组最大值
from typing import List


class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        max_num = max(nums)
        cnt = [0] * (max_num + 1)
        for num in nums:
            cnt[num] += 1

        pre = [0] * (max_num + 1)
        for i in range(1, max_num + 1):
            pre[i] = pre[i-1] + cnt[i]

        total = 0
        for y in range(1, max_num + 1):
            if cnt[y]:
                d = 1
                while d * y <= max_num:
                    total += cnt[y] * d * (pre[min(max_num, (d+1) * y - 1)] - pre[d*y - 1])
                    d += 1
        return total % (10**9 + 7)


sol = Solution()
nums = [7] * 7
print(sol.sumOfFlooredPairs(nums))
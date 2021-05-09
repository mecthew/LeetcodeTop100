# -*-coding:utf-8-*-
"""
@Time    : 2021/5/9 10:52
@Author  : Mecthew
@File    : 5752. 子数组最小乘积的最大值.py
"""
from typing import List

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_min_p = 0

        left, right = [-1] * n, [n] * n
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                left[i] = i - 1
            elif nums[i] == nums[i-1]:
                left[i] = left[i-1]
            else:
                idx = left[i-1]
                while idx != -1 and nums[idx] >= nums[i]:
                    idx = left[idx]
                left[i] = idx

            if nums[n-i-1] > nums[n-i]:
                right[n-i-1] = n - i
            elif nums[n-i-1] == nums[n-i]:
                right[n-i-1] = right[n-i]
            else:
                idx = right[n-i]
                while idx != n and nums[idx] >= nums[n-i-1]:
                    idx = right[idx]
                right[n-i-1] = idx

        # print(left, right)
        acc_sum = [0] * n
        for i, num in enumerate(nums):
            if i == 0:
                acc_sum[i] = num
            else:
                acc_sum[i] = acc_sum[i-1] + num

        for i, num in enumerate(nums):
            if left[i] == -1:
                max_min_p = max(max_min_p, num * (acc_sum[right[i]-1]))
            else:
                max_min_p = max(max_min_p, num * (acc_sum[right[i]-1] - acc_sum[left[i]]))

        return max_min_p % (10**9 + 7)


sol = Solution()
nums = [2,5,4,2,4,5,3,1,2,4]
print(sol.maxSumMinProduct(nums))
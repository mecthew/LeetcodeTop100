from typing import List
# Medium

class Solution:
    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        left, right = [1] * len(nums), [1] * len(nums)
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
            right[len(nums) - 1 - i] = right[len(nums) - i] * nums[len(nums) - i]

        ret = []
        for i in range(len(nums)):
            ret.append(left[i] * right[i])
        return ret

    # 高级方法，上三角和下三角倒乘
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        p, q = 1, 1
        for i in range(len(nums) - 1):
            p *= nums[i]
            res.append(p)
        for i in range(len(nums)-1, 0, -1):
            q *= nums[i]
            res[i-1] *= q
        return res

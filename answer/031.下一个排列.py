from typing import List
from bisect import bisect_right

# Medium
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        def reverse_array(start, end):
            mid = (start + end) // 2
            for k in range(mid - start + 1):
                nums[start+k], nums[end-k] = nums[end-k], nums[start+k]

        idx = 0
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                idx = i
                break
        if idx == 0:
            reverse_array(0, len(nums)-1)
        else:
            reverse_array(idx, len(nums) - 1)
            for j in range(idx, len(nums)):
                if nums[j] > nums[idx-1]:
                    nums[j], nums[idx-1] = nums[idx-1], nums[j]
                    break


    def nextPermutation1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n-2, -1, -1):
            idx = bisect_right(nums, nums[i], i+1, n)
            if idx == n:
                tmp = nums[i]
                for j in range(i, idx-1):
                    nums[j] = nums[j+1]
                nums[idx-1] = tmp
            else:
                nums[i], nums[idx] = nums[idx], nums[i]
                break

sol = Solution()
nums = [1, 3, 2]
sol.nextPermutation(nums)
print(nums)


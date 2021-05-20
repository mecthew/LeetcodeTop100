from typing import List
# Medium
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left, right = -1, -1
        min_val, max_val = None, None

        for ith in range(len(nums)):
            if left == -1 and ith + 1 < len(nums) and nums[ith] > nums[ith + 1]:
                left = ith
                right = ith + 1
                max_val = nums[ith]
                min_val = nums[ith + 1]
            elif ith + 1 < len(nums) and nums[ith] > nums[ith + 1]:
                right = ith + 1
                max_val = max(max_val, nums[ith])
                min_val = min(min_val, nums[ith + 1])
                while left > 0 and min_val < nums[left - 1]:
                    left -= 1
            elif max_val is not None and nums[ith] < max_val:
                right = ith
                min_val = min(min_val, nums[ith])
                while left > 0 and min_val < nums[left - 1]:
                    left -= 1

        return 0 if left == -1 else right - left + 1


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 3, 2, 2, 2]
    print(sol.findUnsortedSubarray(nums))
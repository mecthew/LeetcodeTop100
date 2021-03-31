from typing import List

# Medium
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        ret = set()
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            if nums[i] > 0:     # 最小的数大于0时即结束
                break

            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum == 0:
                    ret.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    right -= 1

        return list(map(list, ret))

sol = Solution()
nums = [-1,0,1,2,-1,-4]
print(sol.threeSum(nums))

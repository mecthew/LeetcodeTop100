from typing import List
# Medium

# 要求O(1)空间复杂度,这里有个前提是num \in [1, n]，长度为n+1
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ans = -1
        left, right = 1, len(nums)-1
        while left <= right:
            mid = (left + right) >> 1
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1

            if cnt <= mid:
                left = mid + 1
            else:
                right = mid - 1
                ans = mid
        return ans


sol = Solution()
nums = [1,3,4,4,4]
print(sol.findDuplicate(nums))

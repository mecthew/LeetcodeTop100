from typing import List
# Easy, solve it without extra space and in O(n) runtime?
# You may assume the returned list does not count as extra space.

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            num %= len(nums) + 1

            nums[num - 1] += len(nums) + 1

        ret = [idx+1 for idx, num in enumerate(nums) if num < len(nums) + 1]
        return ret


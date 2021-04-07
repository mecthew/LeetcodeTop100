from typing import List
# Medium

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bisect_left(start, end, tgt):
            while start < end:
                mid = (start + end) // 2
                if nums[mid] < tgt:
                    start = mid + 1
                else:
                    end = mid
            return end

        lidx = bisect_left(0, len(nums)-1, target)
        if lidx == -1 or nums[lidx] != target:
            return [-1, -1]
        else:
            i = lidx + 1
            while i < len(nums):
                if nums[i] != target:
                    break
                i += 1
            return [lidx, i-1]

from typing import List
# Medium

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, pprev = 0, 0
        ret = 0

        for num in nums:
            prev, pprev = max(prev, pprev + num), prev
            ret = max(ret, prev)
        return ret


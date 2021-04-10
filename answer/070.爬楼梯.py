from typing import List
# Easy

class Solution:
    def climbStairs(self, n: int) -> int:
        pprev, prev = 0, 1
        for i in range(n):
            cur = pprev + prev
            pprev, prev = prev, cur
        return prev

# encoding: utf-8
"""
@Time    : 2021/4/11 10:48
@Author  : Mecthew
@File    : 最少侧跳次数.py
"""
from typing import List
import sys

class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        dp = [1, 0, 1]

        for ith, obs in enumerate(obstacles[1:], 1):
            if obs:
                dp[obs-1] = sys.maxsize

            dp[0] = min(dp[0], dp[1]+1, dp[2]+1)
            dp[1] = min(dp[1], dp[0]+1, dp[2]+1)
            dp[2] = min(dp[2], dp[0]+1, dp[1]+1)

            if obs:
                dp[obs-1] = sys.maxsize
            print(dp)
        return min(dp)


sol = Solution()
obstacles = [0,1,2,3,0]
sol.minSideJumps(obstacles)
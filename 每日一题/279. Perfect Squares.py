# -*-coding:utf-8-*-
"""
@Time    : 2021/6/11 10:24
@Author  : Mecthew
@File    : 279. Perfect Squares.py
"""

import math
import sys
class Solution:
    def numSquares(self, n: int) -> int:
        if int(math.sqrt(n))**2 == n:
            return 1

        dp = [i for i in range(n+1)]
        for i in range(2, int(math.sqrt(n)) + 1):
            for j in range(i**2, n+1):
                dp[j] = min(dp[j], dp[j - i**2] + 1)
                if j == n and dp[j] == 2:
                    return 2
        # print(dp)
        return dp[n]


sol = Solution()
print(sol.numSquares(2021))

from typing import List
# Medium

import math
import sys


class Solution:
    def numSquares(self, n: int) -> int:
        if int(math.sqrt(n)) ** 2 == n:
            return 1

        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            min_cnt = sys.maxsize
            for j in range(1, int(math.sqrt(i)) + 1):
                min_cnt = min(min_cnt, 1 + dp[i - j ** 2])
            dp[i] = min_cnt
        return dp[n]



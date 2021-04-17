from typing import List
# Medium

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1] * (n+1)
        for i in range(2, n+1):
            num = 0
            for j in range(1, i+1):
                num += dp[j-1] * dp[i-j]
            dp[i] = num
        return dp[n]


sol = Solution()
print(sol.numTrees(1))
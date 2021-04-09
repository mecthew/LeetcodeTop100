from typing import List
# Medium,与62相似

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        for j in range(n-1, -1, -1):
            dp[j] = grid[-1][j] if j == n-1 else dp[j+1] + grid[-1][j]

        for i in range(m-2, -1, -1):
            for j in range(n-1, -1, -1):
                dp[j] = grid[i][j] + (dp[j] if j == n-1 else min(dp[j], dp[j+1]))
        return dp[0]

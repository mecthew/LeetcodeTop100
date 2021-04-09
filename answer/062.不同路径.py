from typing import List
# Medium，从矩阵左上角到右下角的路径数
class Solution:
    # 空间可优化
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n

        for i in range(m-2, -1, -1):
            for j in range(n-1, -1, -1):
                dp[j] = dp[j] if j == n-1 else dp[j] + dp[j+1]
        return dp[0]
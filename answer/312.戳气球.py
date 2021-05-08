from typing import List
import sys


# Hard

class Solution:
    # i,j开区间，假设k是最后一个被戳破的气球，则状态转移公式dp[i][j] = dp[i][k] + nums[i]*nums[k]*nums[j] + dp[k][j]
    #(这里重点是i,j不动，k作为最后一个)
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                max_coin = 0
                for k in range(i+1, j):
                    max_coin = max(max_coin, dp[i][k] + nums[i] * nums[k] * nums[j] + dp[k][j])
                dp[i][j] = max_coin
        # print(dp)
        return dp[0][n-1]


sol = Solution()
nums = [3, 1, 5, 8]
print(sol.maxCoins(nums))

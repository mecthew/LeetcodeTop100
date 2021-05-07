from typing import List
# Medium
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * 3
        for ith, price in enumerate(prices):
            if ith == 0:
                dp[0] = -price
            else:
                dp[0], dp[1], dp[2] = max(dp[0], dp[1]-price), max(dp[1], dp[2]), dp[0] + price
        return max(dp)
from typing import List
# Easy

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]

        max_profit = 0
        for price in prices[1:]:
            max_profit = max(max_profit, price - min_val)
            min_val = min(min_val, price)
        return max_profit
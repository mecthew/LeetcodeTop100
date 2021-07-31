# -*-coding:utf-8-*-
"""
@Time    : 2021/6/10 11:43
@Author  : Mecthew
@File    : 518. Coin Change 2.py
"""
from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] = dp[j] + dp[j - coin]
        return dp[amount]


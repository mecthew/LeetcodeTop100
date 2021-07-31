# -*-coding:utf-8-*-
"""
@Time    : 2021/6/8 15:46
@Author  : Mecthew
@File    : 1049. Last Stone Weight II.py
"""
from typing import List
import heapq

# 背包问题：最后剩下的石头一定可以表示成 $\sum_i k_i \cdot stone_i, k_i \in [-1, 1]$，因而可将其划分为pos，neg两堆，目标是min(pos - neg)，
# 即 min(sum - 2neg)，注意最后结果非负，所以neg <= sum // 2，通过背包动态规划解决
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        bound = total // 2
        dp = [False] * (bound + 1)
        dp[0] = True
        max_neg = 0
        for stone in stones:
            for j in range(bound, stone-1, -1):
                dp[j] = dp[j] or dp[j - stone]
                if dp[j] and j > max_neg:
                    max_neg = j
        return total - 2 * max_neg



sol = Solution()
stones = [31,26,33,21,40]
print(sol.lastStoneWeightII(stones))

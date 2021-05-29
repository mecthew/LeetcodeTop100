# -*-coding:utf-8-*-
"""
@Time    : 2021/5/23 11:47
@Author  : Mecthew
@File    : 5766. 石子游戏 VIII.py
"""
from typing import List
import sys
import itertools


class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        pre = list(itertools.accumulate(stones))    # 计算前缀和
        n = len(stones)
        f = pre[-1]
        for ith in range(n-2, 0, -1):
            f = max(f, pre[ith] - f)

        return f


sol = Solution()
stones = [7,-6,5,10,5,-2,-6]
# stones = [-1,2,-3,4,-5]
print(sol.stoneGameVIII(stones))

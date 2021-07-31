# -*-coding:utf-8-*-
"""
@Time    : 2021/6/12 11:36
@Author  : Mecthew
@File    : 1449. Form Largest Integer With Digits That Add up to Target.py
"""
from typing import List
import sys

class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [''] * (target + 1)
        dp[0] = '0'

        for i, c in enumerate(cost):
            for j in range(c, target + 1):
                if dp[j - c]:
                    if dp[j-c] == '0':
                        pnum = str(i+1)
                    else:
                        pnum = str(i+1) + dp[j-c]

                    if dp[j] == '' or int(pnum) > int(dp[j]):
                        dp[j] = pnum

        return '0' if dp[target] == '' else dp[target]


cost = [2,4,6,2,4,6,4,4,4]; target = 5
sol = Solution()
print(sol.largestNumber(cost, target))



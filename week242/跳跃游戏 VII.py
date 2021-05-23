# -*-coding:utf-8-*-
"""
@Time    : 2021/5/23 11:17
@Author  : Mecthew
@File    : 跳跃游戏 VII.py
"""
from bisect import bisect_left, bisect_right


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        dp = [0]
        n = len(s)
        for ith, ch in enumerate(s[1:], 1):
            if ch == '0':
                left, right = ith - maxJump, ith - minJump
                left_idx = bisect_left(dp, left)
                right_idx = bisect_right(dp, right)
                if left_idx < right_idx:
                    dp.append(ith)
        return (n-1) in dp


sol = Solution()
s = "01101110"; minJump = 4; maxJump = 4
print(sol.canReach(s, minJump, maxJump))


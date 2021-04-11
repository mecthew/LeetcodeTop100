# encoding: utf-8
"""
@Time    : 2021/4/11 10:37
@Author  : Mecthew
@File    : 找出游戏的获胜者.py
"""


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def dfs_search(size: int):
            if size == 1:
                return 1
            else:
                prev_i = (dfs_search(size-1) + (k % size)) % size
                if prev_i == 0:
                    return size
                else:
                    return prev_i
        return dfs_search(n)

sol = Solution()
print(sol.findTheWinner(5, 2))
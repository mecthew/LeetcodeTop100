# -*-coding:utf-8-*-
"""
@Time    : 2021/6/12 20:12
@Author  : Mecthew
@File    : 887. Super Egg Drop.py
"""


class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(k + 1)]

        for i in range(1, k+1):
            for j in range(1, n+1):
                if i == 1:
                    dp[i][j] = j
                else:
                    left, right = 1, j
                    while left < right - 1:
                        mid = (left + right) // 2
                        if dp[i-1][mid - 1] < dp[i][j - mid]:
                            left = mid
                        elif dp[i-1][mid - 1] == dp[i][j - mid]:
                            left = right = mid
                        else:
                            right = mid - 1
                    dp[i][j] = 1 + min(max(dp[i-1][left-1], dp[i][j-left]), max(dp[i-1][right-1], dp[i][j-right]))
        return dp[k][n]


sol = Solution()
k = 2; n = 6
print(sol.superEggDrop(k, n))
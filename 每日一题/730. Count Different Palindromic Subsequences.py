# -*-coding:utf-8-*-
"""
@Time    : 2021/6/13 20:26
@Author  : Mecthew
@File    : 730. Count Different Palindromic Subsequences.py
"""

class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        A = [ord(ch) - ord('a') for ch in s]
        prev = [[] for _ in range(n)]
        last = [-1] * 4
        for i in range(n):
            prev[i] = last.copy()
            last[A[i]] = i

        last = [n] * 4
        nxt = [[] for _ in range(n)]
        for i in range(n-1, -1, -1):
            nxt[i] = last.copy()
            last[A[i]] = i

        print(prev, '\n', nxt)
        mod = 10**9 + 7
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                else:
                    if s[i] == s[j]:
                        nxt_i = nxt[i][ord(s[i]) - ord('a')]
                        prev_j = prev[j][ord(s[i]) - ord('a')]

                        if i < nxt_i < j and i < prev_j < j and nxt_i != prev_j:
                            dp[i][j] = (2 * dp[i+1][j-1] - dp[nxt_i + 1][prev_j - 1])
                        elif i < nxt_i < j or i < prev_j < j:
                            dp[i][j] = (2 * dp[i + 1][j - 1] + 1)
                        else:
                            dp[i][j] = (2 * dp[i + 1][j - 1] + 2)
                    else:
                        dp[i][j] = (dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1])
        return dp[0][n-1] % mod



sol = Solution()
s = "bccb"
print(sol.countPalindromicSubsequences(s))
from typing import List

# Medium
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        total = 0
        dp = [[True]*n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == n-1:
                    flag = True
                elif j == 0:
                    flag = True
                else:
                    flag = dp[i+1][j-1]
                dp[i][j] = s[i] == s[j] and flag
                total += 1 if dp[i][j] else 0
        return total
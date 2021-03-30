from typing import List
# Medium

# 这道题主要是要区分主串和子序列，字串可以用bool型判断即可
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 1
        start = 0
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                dp[i][j] = (s[i] == s[j]) and (j - i < 3 or dp[i+1][j-1])
                
                if dp[i][j]:
                    if max_len < j - i + 1:
                        max_len = j - i + 1
                        start = i
        return s[start: start+max_len]


s = "aacabdkacaa"
sol = Solution()
print(sol.longestPalindrome(s))

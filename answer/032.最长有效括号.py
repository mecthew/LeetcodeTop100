from typing import List
# Hard

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        for i in range(2, n+1):
            if s[i-1] == ')':
                if s[i-2] == '(':
                    dp[i] = dp[i-2] + 2
                else:
                    if dp[i-1] and i - dp[i-1] - 2 >= 0 and s[i - dp[i-1] - 2] == '(':
                        dp[i] = dp[i-1] + 2 + dp[i - dp[i-1] - 2]

        return max(dp)


    def longestValidParentheses1(self, s: str) -> int:
        stack = []
        prev_len = 0
        longest_len = 0

        for ch in s:
            if ch == '(':
                stack.append(prev_len)
                prev_len = 0
            else:
                if stack:
                    prev_match = stack.pop(-1)
                    prev_len += prev_match + 2

                else:
                    legal = False
                    prev_len = 0
                longest_len = max(prev_len, longest_len)
        return longest_len


sol = Solution()
print(sol.longestValidParentheses("()(()))"))
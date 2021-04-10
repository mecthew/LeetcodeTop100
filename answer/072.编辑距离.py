from typing import List
# Hard
"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/edit-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    # 动态规划，但每次只依赖（1，-1），（-1，0），（0， -1）的值
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [list(range(len(word2) + 1)) for _ in range(2)]

        n, m = len(word1), len(word2)
        for i in range(1, n + 1):
            for j in range(m + 1):
                if j == 0:
                    dp[1][j] = dp[0][j] + 1
                elif word1[i-1] == word2[j-1]:
                    dp[1][j] = dp[0][j-1]
                else:
                    dp[1][j] = min(dp[0][j-1], dp[0][j], dp[1][j-1]) + 1
            print(dp[0], dp[1])
            dp[0] = dp[1].copy()

        return dp[0][m] if n == 0 else dp[1][m]


sol = Solution()
word1 = "a"
word2 = "ab"
print(sol.minDistance(word1, word2))


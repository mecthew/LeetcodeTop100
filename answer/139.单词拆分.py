from typing import List
# Medium
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)

        dp = [False] * n
        dp.append(True)
        for i in range(n-1, -1, -1):
            for j in range(i+1, n+1):
                if dp[j] and s[i: j] in word_set:
                    dp[i] = True
                    break
        return dp[0]



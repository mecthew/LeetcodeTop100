from typing import List
# Hard
# 动态规划匹配，遇到*分情况讨论
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        match = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        match[0][0] = True

        slen, plen = len(s), len(p)
        for i in range(1, plen+1):
            for j in range(slen+1):
                if j == 0:
                    if p[i-1] == '*' and i-2 >= 0 and match[i-2][0]:
                        match[i][0] = True
                else:
                    if match[i-1][j-1] and (p[i-1] == s[j-1] or p[i-1] == '.'):
                        match[i][j] = True
                    elif p[i-1] == '*' and i-2 >= 0:
                        if p[i-2] == '.':
                            match[i][j] = match[i][j-1] or match[i-2][j-1] or match[i-2][j]
                        else:
                            match[i][j] = ((match[i][j-1] or match[i-2][j-1]) and s[j-1] == p[i-2]) or match[i-2][j]

        print(match)
        return match[len(p)][len(s)]


sol = Solution()
s = "aa"
p = '**'
print(sol.isMatch(s, p))
from typing import List
from collections import Counter

# Hard
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        need_cnt = len(t)

        i = 0
        ret = (0, float('inf'))
        for j, ch in enumerate(s):
            if need.get(ch, 0) > 0:
                need_cnt -= 1
            if ch in need:
                need[ch] -= 1

            if need_cnt == 0:
                while i < j:
                    if s[i] not in need or need[s[i]] < 0:
                        if s[i] in need:
                            need[s[i]] += 1
                    else:
                        break
                    i += 1
                if j-i < ret[1]-ret[0]:
                    ret = (i, j)
                if s[i] in need:
                    need[s[i]] += 1
                i += 1
                need_cnt += 1

        return '' if ret[1] >= len(s) else s[ret[0]: ret[1]+1]


sol = Solution()
s = "ADOBECODEBANC"; t = "ABC"
print(sol.minWindow(s, t))
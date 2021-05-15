from typing import List
from collections import Counter

# Medium, O(26 * n)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ret = []
        counter = Counter(p)

        for i in range(len(s)):
            if i >= len(p):
                if s[i - len(p)] in counter:
                    counter[s[i - len(p)]] += 1

            if s[i] in counter:
                counter[s[i]] -= 1

            if all(v == 0 for v in counter.values()):
                ret.append(i - len(p) + 1)
        return ret


sol = Solution()
s = "cbaebabacd"
p = "abc"
print(sol.findAnagrams(s, p))

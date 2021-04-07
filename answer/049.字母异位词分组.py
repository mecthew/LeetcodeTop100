from typing import List
from collections import defaultdict
# Medium

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dic = defaultdict(list)
        for s in strs:
            inc_order = ''.join(sorted(s))
            anagrams_dic[inc_order].append(s)

        return list(anagrams_dic.values())


sol = Solution()
strs = ["",""]
print(sol.groupAnagrams(strs))

from typing import List
# Medium
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chs = set()
        max_len = 0
        left = 0
        for ith, ch in enumerate(s):
            if ch not in chs:
                chs.add(ch)
            else:
                while s[ith] in chs:
                    chs.remove(s[left])
                    left += 1
                chs.add(ch)
            max_len = max(len(chs), max_len)
        return max_len

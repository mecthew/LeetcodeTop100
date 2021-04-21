from typing import List

# Hard
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        len_dict = {}
        max_len = 0
        for num in nums:
            if num not in len_dict:
                left_len = len_dict.get(num-1, 0)
                right_len = len_dict.get(num+1, 0)
                cur_len = left_len + 1 + right_len
                max_len = max(max_len, cur_len)
                len_dict[num] = cur_len
                len_dict[num-left_len] = cur_len
                len_dict[num+right_len] = cur_len

        return max_len
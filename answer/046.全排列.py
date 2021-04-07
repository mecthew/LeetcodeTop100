from typing import List
import itertools

# Medium
class Solution:
    # nums中每个数字都是独特的
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        def dfs_permute(prev_list, contain_set):
            for num in nums:
                if num not in contain_set:
                    dfs_permute(prev_list + [num], contain_set + {num})
            if len(contain_set) == len(nums):
                ret.append(prev_list)
        dfs_permute([], {})
        # return list(itertools.permutations(nums))
        return ret

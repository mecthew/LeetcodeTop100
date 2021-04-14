from typing import List
# Medium

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ret_list = []
        def dfs_subsets(idx, prev_set):
            if idx == len(nums):
                ret_list.append(prev_set)
            else:
                next_set = prev_set.copy() + [nums[idx]]
                dfs_subsets(idx+1, prev_set)
                dfs_subsets(idx+1, next_set)
        dfs_subsets(0, [])
        return ret_list

sol = Solution()
nums = [1,2,3]
print(sol.subsets(nums))

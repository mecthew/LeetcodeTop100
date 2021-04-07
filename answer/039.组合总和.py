from typing import List
import sys
# Medium

class Solution:
    # 动态，也可以用回溯法
    def combinationSum1(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        N = len(candidates)
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]

        for i in range(1, N+1):
            for j in range(candidates[i-1], target+1):
                dp[j] += list(map(lambda x: x + [candidates[i-1]], dp[j-candidates[i-1]]))

        return dp[target]

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        candidates.sort()

        def dfs_search(idx, remain, prev_list):
            if remain == 0:
                ret.append(prev_list)
            elif idx == len(candidates) or candidates[idx] > remain:
                return
            else:
                dfs_search(idx, remain-candidates[idx], prev_list + [candidates[idx]])
                dfs_search(idx+1, remain, prev_list)
        dfs_search(0, target, [])
        return ret


sol = Solution()
candidates = [1]; target = 11
print(sol.combinationSum(candidates, target))

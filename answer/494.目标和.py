from typing import List
# Medium，可转换为0，1背包
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        ntarget = (sum(nums) + target) // 2
        if (sum(nums) + target) % 2 != 0:
            return 0
        dp = [0] * (ntarget + 1)
        dp[0] = 1       # 这里为1，表示不存在加号
        for num in nums:
            for t in range(ntarget, num-1, -1):
                dp[t] = dp[t] + dp[t - num]

        return dp[ntarget]


sol = Solution()
nums = [1]
target = 2
print(sol.findTargetSumWays(nums, target))
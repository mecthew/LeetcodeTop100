from typing import List

# Medium 背包问题
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        num_sum = sum(nums)
        if num_sum % 2 == 1:
            return False

        target_sum = num_sum // 2

        n = len(nums)
        dp = [False] * (target_sum + 1)
        dp[0] = True
        for i in range(n):
            for j in range(target_sum, nums[i]-1, -1):
                dp[j] = dp[j] or dp[j - nums[i]]
                if dp[target_sum] is True:
                    return True
        return False


if __name__ == '__main__':
    # print(float('-inf'))
    nums = [8, 4]
    sol = Solution()
    print(sol.canPartition(nums))

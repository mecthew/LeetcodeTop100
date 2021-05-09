from typing import List
# Medium

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [-1] * amount
        for a in range(amount):
            for coin in coins:
                if a + 1 == coin:
                    dp[a] = 1
                    break
                else:
                    if a - coin >= 0 and dp[a - coin] > 0:
                        if dp[a] == -1:
                            dp[a] = dp[a - coin] + 1
                        else:
                            dp[a] = min(dp[a], dp[a - coin] + 1)
        # print(dp)
        return dp[-1]


coins = [1,2,5]
amount = 11
sol = Solution()
print(sol.coinChange(coins, amount))
# -*-coding:utf-8-*-
"""
@Time    : 2021/6/9 11:26
@Author  : Mecthew
@File    : 879. Profitable Schemes.py

There is a group of n members, and a list of various crimes they could commit. The ith crime generates a profit[i] and
 requires group[i] members to participate in it. If a member participates in one crime, that member can't participate in another crime.

Let's call a profitable scheme any subset of these crimes that generates at least minProfit profit, and the total number
 of members participating in that subset of crimes is at most n.

Return the number of schemes that can be chosen. Since the answer may be very large, return it modulo 109 + 7.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/profitable-schemes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        dp = [[0] * (minProfit + 1) for _ in range(n+1)]
        dp[0][0] = 1

        for i in range(len(group)):
            for j in range(n, group[i]-1, -1):
                for k in range(minProfit, -1, -1):
                    dp[j][k] = dp[j][k] + dp[j-group[i]][max(0, k-profit[i])]

        return sum(dp[i][minProfit] for i in range(n+1)) % (10**9 + 7)


sol = Solution()
n = 10; minProfit = 5; group = [2, 3, 5]; profit = [6, 7, 8]
print(sol.profitableSchemes(n, minProfit, group, profit))
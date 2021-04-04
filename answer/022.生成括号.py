from typing import List
# Medium

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [[] for _ in range(n + 1)]  # dp[i]存放i组括号的所有有效组合
        dp[0] = [""]  # 初始化dp[0]
        for i in range(1, n + 1):  # 计算dp[i]
            for p in range(i):  # 遍历p
                l1 = dp[p]  # 得到dp[p]的所有有效组合
                l2 = dp[i - 1 - p]  # 得到dp[q]的所有有效组合，两者组合不存在重复情况
                for k1 in l1:
                    for k2 in l2:
                        dp[i].append("({0}){1}".format(k1, k2))

        return dp[n]



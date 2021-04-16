from typing import List
# Hard

# the same as 84
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [0] * (n + 2)  # insert zero in

        ret = 0
        for i in range(m):
            stack = [0]
            for j in range(1, len(dp)):
                if j-1 < n and matrix[i][j-1] == '1':
                    dp[j] += 1
                else:
                    dp[j] = 0

                while stack and dp[stack[-1]] > dp[j]:
                    idx = stack.pop(-1)
                    height = dp[idx]
                    ret = max(ret, height * (j - stack[-1] - 1))
                stack.append(j)
        return ret


sol = Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(sol.maximalRectangle(matrix))

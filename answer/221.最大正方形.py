from typing import List
import math
# Medium

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        M, N = len(matrix), len(matrix[0])
        height = [0] * (N + 2)
        max_square = 0
        for i in range(M):
            stack = [0]
            for j in range(1, N+2):
                if j <= N:
                    height[j] = 0 if matrix[i][j-1] == '0' else height[j] + 1
                while stack and height[stack[-1]] >= height[j]:
                    idx = stack.pop(-1)
                    h = height[idx]
                    l = j - stack[-1] - 1 if stack else j
                    cur_square = min(h * h, l * l)
                    max_square = max(max_square, cur_square)
                stack.append(j)
        return max_square


sol = Solution()
matrix = [["0"]]
print(sol.maximalSquare(matrix))
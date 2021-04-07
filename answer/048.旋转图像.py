from typing import List

"""
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
"""

# Medium，顺时针旋转非空 nxn 二维矩阵90度
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def rotate_mv(top, bottom, left, right):
            if top >= bottom or left >= right:
                return
            else:
                tmp = matrix[top][left+1: right+1]
                for i in range(left+1, right+1):
                    offset = i-left
                    matrix[top][i] = matrix[bottom-offset][left]
                for i in range(top, bottom):
                    offset = i - top
                    matrix[i][left] = matrix[bottom][left+offset]
                for i in range(left, right):
                    offset = i-left
                    matrix[bottom][i] = matrix[bottom-offset][right]
                for i in range(top+1, bottom+1):
                    offset = i - (top+1)
                    matrix[i][right] = tmp[offset]
                rotate_mv(top+1, bottom-1, left+1, right-1)
        rotate_mv(0, len(matrix)-1, 0, len(matrix[0])-1)


sol = Solution()
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
sol.rotate(matrix)

print(matrix)


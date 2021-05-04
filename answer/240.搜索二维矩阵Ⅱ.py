from typing import List
# Medium

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(left, right, top, bottom):
            if left > right or top > bottom:
                return False
            else:
                val = matrix[top][right]
                if val == target:
                    return True
                elif val < target:
                    return search(left, right, top+1, bottom)
                else:
                    return search(left, right-1, top, bottom)
        return search(0, len(matrix[0]), 0, len(matrix))
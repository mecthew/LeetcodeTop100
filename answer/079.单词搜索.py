from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        def dfs_search(i, j, idx):
            if idx == len(word):
                return True
            elif i < 0 or i >= m or j < 0 or j >= n:
                return False
            else:
                if word[idx] != board[i][j]:
                    return False
                else:
                    board[i][j] = '#'
                    for direct in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        if dfs_search(i+direct[0], j+direct[1], idx+1):
                            return True
                    board[i][j] = word[idx]
                    return False

        for row in range(m):
            for col in range(n):
                if dfs_search(row, col, 0):
                    return True
        return False


sol = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]; word = "ABCCED"
print(sol.exist(board, word))

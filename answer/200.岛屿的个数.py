from typing import List
# Medium
class UnionSet(object):

    def __init__(self, size):
        self.father = [i for i in range(size)]
        self.depth = [1] * size

    def find(self, x):
        if x == self.father[x]:
            return x
        else:
            self.father[x] = self.find(self.father[x])
            return self.father[x]

    def union(self, x, y):
        xf, yf = self.find(x), self.find(y)
        if xf != yf:
            if self.depth[xf] < self.depth[yf]:
                self.father[xf] = yf
            else:
                self.father[yf] = xf

            if self.depth[xf] == self.depth[yf]:
                self.depth[xf] += 1

class Solution:
    # dfs方法
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs_search(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return
            elif grid[r][c] in ['0', '2']:
                return
            else:
                grid[r][c] = '2'
                dfs_search(r, c+1)
                dfs_search(r, c-1)
                dfs_search(r+1, c)
                dfs_search(r-1, c)

        ret = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ret += 1
                    dfs_search(i, j)
        return ret

    # 并查集方法
    def numIslands1(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        unionset = UnionSet(m*n)
        root_set = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    idx = i * n + j
                    for direct in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                        i_next = i + direct[0]
                        j_next = j + direct[1]
                        if 0 <= i_next < m and 0 <= j_next < n and grid[i_next][j_next] == '1':
                            idx_next = i_next * n + j_next
                            unionset.union(idx, idx_next)
                    if unionset.find(idx) not in root_set:
                        root_set.add(unionset.find(idx))
        return len(set(unionset.find(idx) for idx in root_set))


sol = Solution()
grid = [["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]]
print(sol.numIslands(grid))
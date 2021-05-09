# -*-coding:utf-8-*-
"""
@Time    : 2021/5/9 11:30
@Author  : Mecthew
@File    : 5753. 有向图中最大颜色值.py
"""
from typing import List
from collections import defaultdict

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        indeg = [0] * n
        for v, u in edges:
            indeg[u] += 1
            graph[v].append(u)

        queue = [i for i in range(n) if indeg[i] == 0]
        dp = [[0]*26 for _ in range(n)]
        found = 0
        while queue:
            v = queue.pop(0)
            dp[v][ord(colors[v]) - ord('a')] += 1
            found += 1

            for u in graph[v]:
                for j in range(26):
                    dp[u][j] = max(dp[u][j], dp[v][j])
                indeg[u] -= 1
                if indeg[u] == 0:
                    queue.append(u)

        if found < n:
            return -1
        else:
            max_color_num = 0
            for i in range(n):
                max_color_num = max(max_color_num, max(dp[i]))
            return max_color_num

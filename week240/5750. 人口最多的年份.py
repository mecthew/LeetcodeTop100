# -*-coding:utf-8-*-
"""
@Time    : 2021/5/9 10:42
@Author  : Mecthew
@File    : 5750. 人口最多的年份.py
"""
from typing import List

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        births = [log[0] for log in logs]
        deaths = [log[1] for log in logs]
        births.sort()
        deaths.sort()

        max_year = None
        max_num = 0
        acc_num = 0

        p1, p2 = 0, 0
        while p1 < len(births):
            acc_num += 1
            while deaths[p2] <= births[p1]:
                p2 += 1
                acc_num -= 1
            if max_num < acc_num:
                max_num = acc_num
                max_year = births[p1]
            p1 += 1

        return max_year


sol = Solution()
logs = [[1950,1961],[1960,1971],[1970,1981]]
print(sol.maximumPopulation(logs))

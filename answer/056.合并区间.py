from typing import List
# Medium

"""
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
"""

# 排序 + 看前一位
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merge = []
        for interval in intervals:
            if not merge or merge[-1][1] < interval[0]:
                merge.append(interval)
            elif interval[1] > merge[-1][1]:
                merge[-1][1] = interval[1]
        return merge

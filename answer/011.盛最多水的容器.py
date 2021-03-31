from typing import List
# Medium
# 双指针解法，主要基于一个事实：面积S(i, j) = min(h[i], h[j]) * (j - i)，只可能去移动短板才可能使得面积增加
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        max_area = 0
        while i < j:
            max_area = max(max_area, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area


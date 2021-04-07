from typing import List
# Hard
"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.
"""

# 这道题其实并不难，主要是找到每个位置左右两边的最高点
class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        left, right = [0] * N, [0] * N
        for i in range(1, N):
            left[i] = max(height[i-1], left[i-1])
            right[N-i-1] = max(height[N-i], right[N-i])

        trap_sum = 0
        for i in range(1, N-1):
            trap_sum += max(min(left[i], right[i]) - height[i], 0)
        return trap_sum

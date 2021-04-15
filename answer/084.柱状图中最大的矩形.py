from typing import List
# Hard

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)
        left = [0] * N
        right = [N-1] * N

        for i in range(1, N):
            if heights[i] == heights[i-1]:
                left[i] = left[i-1]
            elif heights[i] > heights[i-1]:
                left[i] = i
            else:
                idx = left[i-1] - 1
                while idx >= 0 and heights[idx] >= heights[i]:
                    idx = left[idx] - 1
                left[i] = idx + 1

        for i in range(N-2, -1, -1):
            if heights[i] == heights[i+1]:
                right[i] = right[i+1]
            elif heights[i] > heights[i+1]:
                right[i] = i
            else:
                idx = right[i+1] + 1
                while idx < N and heights[idx] >= heights[i]:
                    idx = right[idx] + 1
                right[i] = idx - 1

        max_area = 0
        for i in range(N):
            max_area = max(max_area, heights[i] * (right[i] - left[i] + 1))
        return max_area

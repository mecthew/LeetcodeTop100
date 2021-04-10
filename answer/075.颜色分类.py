from typing import List
# Medium

class Solution:
    # 使用计数排序
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt_array = [0] * 3
        for num in nums:
            cnt_array[num] += 1

        begin_idx = 0
        for ith, cnt in enumerate(cnt_array):
            for j in range(cnt):
                nums[begin_idx + j] = ith
            begin_idx += cnt

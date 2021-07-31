# -*-coding:utf-8-*-
"""
@Time    : 2021/6/10 21:38
@Author  : Mecthew
@File    : 4. Median of Two Sorted Arrays.py
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findKthMin(k):
            idx1, idx2 = 0, 0
            while k > 0:
                if idx1 == len(nums1):
                    return nums2[idx2 + k - 1]
                elif idx2 == len(nums2):
                    return nums1[idx1 + k - 1]
                elif k == 1:
                    return min(nums1[idx1], nums2[idx2])
                else:
                    tidx1 = min(idx1 + k // 2 - 1, len(nums1)-1)
                    tidx2 = min(idx2 + k // 2 - 1, len(nums2)-1)

                    if nums1[tidx1] <= nums2[tidx2]:
                        k -= tidx1 - idx1 + 1
                        idx1 = tidx1 + 1
                    else:
                        k -= tidx2 - idx2 + 1
                        idx2 = tidx2 + 1

        total_cnt = len(nums1) + len(nums2)
        return findKthMin((total_cnt + 1) // 2) if total_cnt & 1 == 1 else (findKthMin(total_cnt // 2) +  findKthMin(total_cnt // 2 + 1)) / 2


sol = Solution()
nums1 = []; nums2 = [3,4]
print(sol.findMedianSortedArrays(nums1, nums2))
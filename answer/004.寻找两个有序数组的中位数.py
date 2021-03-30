from typing import List

# Hard
# 可将问题看成是求解第k小的通用问题，偶数情况则求第k和k+1小的情况，这题难点在于边界情况的界定
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findKthMin(k):
            i1, i2 = 0, 0
            while k > 0:
                if i1 == len(nums1):
                    return nums2[i2 + k - 1]
                if i2 == len(nums2):
                    return nums1[i1 + k - 1]
                if k == 1:
                    return min(nums1[i1], nums2[i2])

                new_i1 = min(n1-1, i1 + k//2 - 1)
                new_i2 = min(n2-1, i2 + k//2 - 1)
                if nums1[new_i1] <= nums2[new_i2]:
                    k -= new_i1 - i1 + 1
                    i1 = new_i1 + 1
                else:
                    k -= new_i2 - i2 + 1
                    i2 = new_i2 + 1

        n1, n2 = len(nums1), len(nums2)
        if (n1 + n2) & 1 == 1:
            return findKthMin((n1 + n2 + 1) // 2)
        else:
            return (findKthMin((n1 + n2) // 2) + findKthMin((n1 + n2) // 2 + 1)) / 2


if __name__ == '__main__':
    sol = Solution()
    nums1 = [2,3,4,5]
    nums2 = [1, 1]
    print(sol.findMedianSortedArrays(nums1, nums2))

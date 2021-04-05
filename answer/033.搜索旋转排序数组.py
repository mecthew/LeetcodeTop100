from typing import List
# Medium

class Solution:
    # 这里的rotate是指向前移动k（0<=k<=nums.length），旋转后变为[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
    # 原数组是distinct且升序的，先搜索两个升序数组的交界点，在两个有序数组再搜索
    def search1(self, nums: List[int], target: int) -> int:
        if len(nums) <= 1:
            return 0 if target in nums else -1

        def search_array(start, end, tgt):
            l, r = start, end
            while l < r:
                _mid = (l + r) // 2
                if nums[_mid] == tgt:
                    return _mid
                elif nums[_mid] < tgt:
                    l = _mid + 1
                else:
                    r = _mid - 1
            return l if l == r and nums[l] == tgt else -1

        left, right = 0, len(nums)-1
        while left < right - 1:
            mid = (left + right) // 2
            if nums[0] <= nums[mid]:
                left = mid
            else:
                right = mid - 1

        max_idx = left if nums[left] > nums[right] else right
        idx1, idx2 = search_array(0, max_idx, target), search_array(max_idx+1, len(nums)-1, target)
        return -1 if idx1 == idx2 == -1 else (idx1 if idx1 != -1 else idx2)

    # 这种方法通过讨论上下界的情况
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = (lo + hi) // 2
            # 前两种情况向后规约
            if nums[0] <= nums[mid] and (target < nums[0] or target > nums[mid]):
                lo = mid + 1
            elif nums[0] > nums[mid] and (nums[mid] < target < nums[0]):
                lo = mid + 1
            else:
                hi = mid
        return lo if lo == hi and nums[lo] == target else -1


sol = Solution()
print(sol.search([4,5], 5))
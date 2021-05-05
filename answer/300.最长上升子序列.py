from typing import List
# Medium

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []
        for num in nums:
            if not lis:
                lis.append(num)
            else:
                left, right = 0, len(lis)-1
                ans = -1
                while left <= right:
                    mid = (left + right) >> 1
                    if lis[mid] >= num:
                        right = mid - 1
                    else:
                        left = mid + 1
                        ans = mid
                if ans + 1 < len(lis):
                    lis[ans + 1] = min(lis[ans+1], num)
                else:
                    lis.append(num)
        return len(lis)
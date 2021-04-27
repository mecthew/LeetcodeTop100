from typing import List

# Easy
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        majority_num = None
        for num in nums:
            if cnt == 0:
                majority_num = num
                cnt += 1
            else:
                cnt += 1 if majority_num == num else -1
        return majority_num
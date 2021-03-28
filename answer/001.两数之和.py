from typing import List
from collections import defaultdict


# Easy
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num2idx = defaultdict(list)
        [num2idx[num].append(idx) for idx, num in enumerate(nums)]
        for num, idxes in num2idx.items():
            if num + num == target and len(idxes) >= 2:
                return idxes[:2]
            elif 2*num != target and target - num in num2idx:
                return [idxes[0], num2idx[target - num][0]]
        return [-1, -1]
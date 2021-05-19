from typing import List
from collections import defaultdict
# Medium

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSum = defaultdict(int)
        preSum[0] = 1
        num_sum = 0
        total = 0
        for num in nums:
            num_sum += num
            total += preSum.get(num_sum - k, 0)
            preSum[num_sum] += 1

        return total


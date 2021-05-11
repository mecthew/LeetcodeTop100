from typing import List
from collections import Counter
import heapq
import sys
# Medium

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 最小堆
        # counter = Counter(nums)
        # cnt_value = [(cnt, value) for value, cnt in counter.items()]
        # min_heap = cnt_value[:k]
        # heapq.heapify(min_heap)
        #
        # for cnt, value in cnt_value[k:]:
        #     heapq.heappushpop(min_heap, (cnt, value))
        # return [v for cnt, v in min_heap]

        # 桶排序
        counter = Counter(nums)
        max_cnt = max(counter.values())
        cnt_as_idx = [[] for _ in range(max_cnt + 1)]
        for num, v in counter.items():
            cnt_as_idx[v].append(num)

        ret = []
        idx = max_cnt
        while len(ret) < k and idx >= 0:
            if cnt_as_idx[idx]:
                ret.extend(cnt_as_idx[idx])
            idx -= 1
        return ret


sol = Solution()
nums = [1, 2]
k = 2
print(sol.topKFrequent(nums, k))

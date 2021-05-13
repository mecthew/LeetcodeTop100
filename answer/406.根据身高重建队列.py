from typing import List
from collections import defaultdict

# Medium
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        ret = []
        for p in people:
            if len(ret) <= p[1]:
                ret.append(p)
            else:
                ret.insert(p[1], p)

        return ret


sol = Solution()
people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
print(sol.reconstructQueue(people))
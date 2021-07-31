# -*-coding:utf-8-*-
"""
@Time    : 2021/6/12 21:19
@Author  : Mecthew
@File    : 354. Russian Doll Envelopes.py
"""
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        lis = [envelopes[0]]
        print(envelopes)
        for env in envelopes[1:]:
            left, right = 0, len(lis) - 1
            while left < right:
                mid = (left + right) // 2
                if lis[mid][1] < env[1]:
                    left = mid + 1
                else:
                    right = mid
            if len(lis) == 1:
                if env[0] > lis[0][0] and env[1] > lis[0][1]:
                    lis.append(env)
                elif lis[0][1] > env[1]:
                    lis[0] = env
            else:
                if left > 0:
                    if lis[left][1] > env[1]:
                        lis[left] = env
                    elif lis[left][1] < env[1]:
                        lis.append(env)
                elif left == 0:
                    lis[left] = env
            # print(lis, left)
        return len(lis)


sol = Solution()
envelopes = [[15,8],[2,20],[2,14],[4,17],[8,19],[8,9],[5,7],[11,19],[8,11],[13,11],[2,13],[11,19],[8,11],[13,11],[2,13],[11,19],[16,1],[18,13],[14,17],[18,19]]
print(sol.maxEnvelopes(envelopes))

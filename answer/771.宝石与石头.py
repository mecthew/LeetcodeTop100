from typing import List
# Easy

import operator
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return len([1 for stone in stones if stone in set(jewels)])

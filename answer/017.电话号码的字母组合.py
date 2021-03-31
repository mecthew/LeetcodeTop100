from typing import List

# Medium
# 时间复杂度和空间复杂度均为O(3^N + 4^M)，N为3个字符的数字数量，M为4个字符的数字数量
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        phone = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        queue = ['']
        for digit in digits:
            new_queue = []
            while queue:
                substr = queue.pop(0)
                for letter in phone[ord(digit) - ord('2')]:
                    new_queue.append(substr + letter)

            queue = new_queue
        return queue


sol = Solution()
print(sol.letterCombinations('222'))

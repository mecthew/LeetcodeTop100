from typing import List


# Easy

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses_dict = {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch in parentheses_dict.keys():
                if len(stack) < 1 or stack[-1] != parentheses_dict[ch]:
                    return False
                else:
                    stack.pop(-1)
            else:
                stack.append(ch)
        return not stack


sol = Solution()
print(sol.isValid('[)'))

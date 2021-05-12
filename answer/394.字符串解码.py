from typing import List
# Medium
class Solution:
    def decodeString(self, s: str) -> str:
        res = ''
        stack = []
        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                target = ''
                while stack and stack[-1] != '[':
                    target = stack.pop(-1) + target
                stack.pop(-1)

                digtis = ''
                while stack and '0' <= stack[-1] <= '9':
                    digtis = stack.pop(-1) + digtis
                digtis = int(digtis)

                stack.append(digtis * target)
        return ''.join(stack)
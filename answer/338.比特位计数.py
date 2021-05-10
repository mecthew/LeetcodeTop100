from typing import List

# Medium，可使用最高比特位方法，动态规划
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0] * (num + 1)
        highbit = 0
        for i in range(1, num):
            if i & (i - 1) == 0:    # 2的整数幂性质
                highbit = i
            res[i] = res[i-highbit] + 1
        return res
        # bits = [0] * 32
        # res = [0]
        # for i in range(1, num+1):
        #     idx = 0
        #     cnt = res[-1]
        #     while idx < 32 and bits[idx] == 1:
        #         bits[idx] = 0
        #         cnt -= 1
        #         idx += 1
        #     bits[idx] = 1
        #     res.append(cnt+1)
        # return res

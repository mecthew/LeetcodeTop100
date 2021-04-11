# encoding: utf-8
"""
@Time    : 2021/4/11 11:05
@Author  : Mecthew
@File    : 求出 MK 平均值.py
"""
import bisect
class MKAverage:

    def __init__(self, m: int, k: int):
        self.m, self.k = m, k
        self.container = []
        self.a = []
        self.num_sum = 0


    def addElement(self, num: int) -> None:
        if len(self.container) == self.m:
            pop_num = self.container.pop(0)
            self.container.append(num)
            self.a.remove(pop_num)
            bisect.insort(self.a, num)
            self.num_sum += num - pop_num
        else:
            self.container.append(num)
            bisect.insort(self.a, num)
            self.num_sum += num

    def calculateMKAverage(self) -> int:
        if len(self.container) < self.m:
            return -1
        else:
            del_sum = sum(self.a[:self.k+1]) + sum(self.a[-self.k:])
            return (self.num_sum - del_sum) // (self.m - 2*self.k)

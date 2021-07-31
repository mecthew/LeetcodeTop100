# -*-coding:utf-8-*-
"""
@Time    : 2021/5/30 11:10
@Author  : Mecthew
@File    : 5774. 使用服务器处理任务.py
"""
from typing import List
import heapq
from collections import defaultdict


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        servers_queue = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(servers_queue)

        release_dict = defaultdict(list)
        block_queue = []
        ret = []
        for i, t in enumerate(tasks):
            if i in release_dict:
                for server in release_dict[i]:
                    heapq.heappush(servers_queue, server)
                del release_dict[i]

            if servers_queue:
                block_queue.append(t)
                while block_queue and servers_queue:
                    time = block_queue.pop(0)
                    pop_item = heapq.heappop(servers_queue)
                    ret.append(pop_item[1])
                    release_dict[i + time].append(pop_item)
            else:
                block_queue.append(t)

        release_times = list(release_dict.keys())
        heapq.heapify(release_times)
        while block_queue:
            prior_time = heapq.heappop(release_times)
            for server in release_dict[prior_time]:
                heapq.heappush(servers_queue, server)
            del release_dict[prior_time]

            while block_queue and servers_queue:
                time = block_queue.pop(0)
                pop_item = heapq.heappop(servers_queue)
                ret.append(pop_item[1])
                if prior_time + time not in release_dict:
                    heapq.heappush(release_times, prior_time + time)
                release_dict[prior_time + time].append(pop_item)

        return ret


if __name__ == '__main__':
    servers = [31,96,73,90,15,11,1,90,72,9,30,88]; tasks = [87,10,3,5,76,74,38,64,16,64,93,95,60,79,54,26,30,44,64,71]
    sol = Solution()
    print(sol.assignTasks(servers, tasks))
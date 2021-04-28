from typing import List
from collections import defaultdict
# Medium

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def indegree_method():
            adj = defaultdict(set)
            indegrees = [0] * numCourses
            for requisity in prerequisites:
                first, second = requisity
                adj[second].add(first)
                indegrees[first] += 1

            zero_queue = [ith for ith in range(numCourses) if indegrees[ith] == 0]
            while zero_queue:
                node = zero_queue.pop(0)
                if node in adj:
                    for subnode in adj[node]:
                        indegrees[subnode] -= 1
                        if indegrees[subnode] == 0:
                            zero_queue.append(subnode)
            return sum(indegrees) == 0

        def dfs_search(root_node, path):
            if root_node in path:
                return False
            else:
                path.add(root_node)
                views[root_node] = True
                if root_node in graph:
                    for subnode in graph[root_node]:
                        if views[subnode] is False:
                            if dfs_search(subnode, path.copy()) is False:
                                return False
                        elif views[subnode] and subnode in path:
                            return False
                return True

        # graph = defaultdict(list)
        # views = [False] * numCourses
        # for requisity in prerequisites:
        #     first, second = requisity
        #     graph[second].append(first)
        #
        # for node in graph.keys():
        #     if views[node] is False:
        #         if dfs_search(node, set()) is False:
        #             return False
        # return True
        return indegree_method()


sol = Solution()
numCourses = 2; prerequisites = [[0,1], [1, 0]]
print(sol.canFinish(numCourses, prerequisites))

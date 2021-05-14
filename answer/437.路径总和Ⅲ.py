from typing import List
# Definition for a binary tree node.
# Medium
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 前缀和解法更佳
class Solution:
    total = 0
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        visited = set()
        def dfs_search(root_node, val):
            if root_node is None:
                return
            else:
                if id(root_node) in visited:
                    have_visit = True
                else:
                    have_visit = False
                    visited.add(id(root_node))
                if root_node.val == val:
                    self.total += 1
                    print(root_node.val)

                dfs_search(root_node.left, val - root_node.val)
                dfs_search(root_node.right, val - root_node.val)
                if not have_visit:
                    dfs_search(root_node.left, targetSum)     # 路径需要连起来
                    dfs_search(root_node.right, targetSum)
        dfs_search(root, targetSum)
        return self.total


sol = Solution()
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node1.right = node2
node2.right = node3
node3.right = node4
node4.right = node5
cnt = sol.pathSum(node1, 3)

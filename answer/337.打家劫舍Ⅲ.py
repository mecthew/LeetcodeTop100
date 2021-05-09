from typing import List
# Medium

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs_rob(root_node):
            if root_node is None:
                return 0, 0
            else:
                left_sum, left_child_sum = dfs_rob(root_node.left)
                right_sum, right_child_sum = dfs_rob(root_node.right)

                max_sum = max(root_node.val + left_child_sum + right_child_sum, left_sum + right_sum)
                return max_sum, left_sum + right_sum
        return dfs_rob(root)[0]
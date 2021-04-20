from typing import List
# Medium

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    prev_node = None

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        def dfs_flatten(root_node):
            if root_node is None:
                if self.prev_node:
                    self.prev_node.left = None
                    self.prev_node.right = None
            else:
                right_node = root_node.right
                if self.prev_node:
                    self.prev_node.right = root_node
                    self.prev_node.left = None

                self.prev_node = root_node
                dfs_flatten(root_node.left)
                dfs_flatten(right_node)
        dfs_flatten(root)
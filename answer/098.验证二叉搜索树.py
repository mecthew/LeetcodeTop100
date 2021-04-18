from typing import List
import sys
# Medium

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    prev_val = -sys.maxsize

    def isValidBST(self, root: TreeNode) -> bool:

        def dfs_search(root_node):
            if root_node.left is None and root_node.right is None:
                flag = self.prev_val < root_node.val
                self.prev_val = root_node.val
                return flag
            else:
                if root_node.left:
                    flag = dfs_search(root_node.left)
                    if not flag:
                        return False

                if self.prev_val >= root_node.val:
                    return False
                self.prev_val = root_node.val
                if root_node.right:
                    flag = dfs_search(root_node.right)
                    if not flag:
                        return False
                return True
        return dfs_search(root)

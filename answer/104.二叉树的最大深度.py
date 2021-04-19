from typing import List
# Easy
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def getDepth(root_node):
            if root_node is None:
                return 0
            else:
                return max(getDepth(root_node.left), getDepth(root_node.right)) + 1
        return getDepth(root)

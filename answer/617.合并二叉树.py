from typing import List

# Easy
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 is None or root2 is None:
            return root1 if root1 else root2
        else:
            root1.val = root1.val + root2.val
            left = self.mergeTrees(root1.left, root2.left)
            right = self.mergeTrees(root1.right, root2.right)
            root1.left = left
            root1.right = right
            return root1
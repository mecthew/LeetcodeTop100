from typing import List
# Easy
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        else:
            tmp_left = root.left
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(tmp_left)
            return root

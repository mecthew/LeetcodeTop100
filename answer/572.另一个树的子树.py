from typing import List
# Easy

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def is_same(root1, root2):
            if root1 is None or root2 is None:
                return root1 is None and root2 is None
            else:
                return root1.val == root2.val and is_same(root1.left, root2.left) and is_same(root1.right, root2.right)
        if root is None or subRoot is None:
            return root is None and subRoot is None
        return is_same(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

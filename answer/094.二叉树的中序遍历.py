from typing import List
# Medium

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []

        def inorder_visit(root_node):
            if root_node is None:
                return
            else:
                inorder_visit(root_node.left)
                ret.append(root_node.val)
                inorder_visit(root_node.right)

        inorder_visit(root)
        return ret

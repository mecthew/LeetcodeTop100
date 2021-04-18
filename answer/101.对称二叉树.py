from typing import List
# Easy
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def checkSymmetric(node1, node2):
            if node1 is None and node2 is None:
                return True
            elif node1 is None or node2 is None:
                return False
            else:
                if not checkSymmetric(node1.left, node2.right):
                    return False

                if node1.val != node2.val:
                    return False

                return checkSymmetric(node1.right, node2.left)

        return checkSymmetric(root.left, root.right)

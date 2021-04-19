from typing import List
# Medium

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue = [(root, 0)]
        prev_depth = -1
        ret = []
        while queue:
            node, depth = queue.pop(0)
            if depth != prev_depth:
                prev_depth = depth
                ret.append([])
            ret[-1].append(node.val)

            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))
        return ret

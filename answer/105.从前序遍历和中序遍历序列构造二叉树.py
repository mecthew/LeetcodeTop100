from typing import List
# Medium

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def recursive_build(pbegin, pend, ibegin, iend):
            if pbegin > pend or ibegin > iend:
                return None
            else:
                root_val = preorder[pbegin]
                idx = inorder.index(root_val)
                root_node = TreeNode(val=root_val)
                left_size = idx - ibegin

                left_node = recursive_build(pbegin+1, pbegin+left_size, ibegin, idx-1)
                right_node = recursive_build(pbegin+left_size+1, pend, idx+1, iend)
                root_node.left = left_node
                root_node.right = right_node
                return root_node
        return recursive_build(0, len(preorder)-1, 0, len(inorder)-1)

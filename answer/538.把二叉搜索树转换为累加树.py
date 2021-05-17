from typing import List
# Medium
from bisect import bisect_left

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 考虑二叉搜索树的性质，右子树的值大于根节点大于左子树
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def dfs_tree(root_node):
            if root_node is None:
                return
            else:
                nonlocal total
                dfs_tree(root_node.right)
                total += root_node.val
                root_node.val = total
                dfs_tree(root_node.left)
        total = 0
        dfs_tree(root)
        return root

    def convertBST1(self, root: TreeNode) -> TreeNode:
        def get_val_list(root_node, val_list):
            if root_node is None:
                return
            else:
                val_list.append(root_node.val)
                get_val_list(root_node.left, val_list)
                get_val_list(root_node.right, val_list)

        def refactor_tree(root_node, val_list):
            if root_node is None:
                return
            else:
                idx = bisect_left(val_list, root_node.val)
                if idx == 0:
                    root_node.val = pre_sum[-1]
                else:
                    root_node.val = pre_sum[-1] - pre_sum[idx - 1]
                refactor_tree(root_node.left, val_list)
                refactor_tree(root_node.right, val_list)

        val_list = []
        get_val_list(root, val_list)
        val_list.sort()
        pre_sum = [0] * len(val_list)
        for ith, val in enumerate(val_list):
            if ith == 0:
                pre_sum[ith] = val
            else:
                pre_sum[ith] = val + pre_sum[ith - 1]

        refactor_tree(root, val_list)
        return root

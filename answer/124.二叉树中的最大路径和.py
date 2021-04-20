from typing import List
# Hard
import sys

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    max_path_sum = -sys.maxsize
    def maxPathSum(self, root: TreeNode) -> int:
        def get_max_path_sum1(root_node):
            if root_node is None:
                return (-sys.maxsize, -sys.maxsize)
            else:
                left_max, left_path_max = get_max_path_sum1(root_node.left)
                right_max, right_path_max = get_max_path_sum1(root_node.right)
                max_sum_with_root = max(root_node.val, root_node.val+left_path_max, root_node.val+right_path_max,
                                        root_node.val + left_path_max + right_path_max
                                        )
                root_path_max = max(root_node.val, root_node.val + left_path_max, root_node.val + right_path_max)
                self.max_path_sum = max(self.max_path_sum, max_sum_with_root, left_max, right_max)
                return (max_sum_with_root, root_path_max)

        def get_max_path_sum(root_node):
            if root_node is None:
                return 0
            else:
                lm = get_max_path_sum(root_node.left)
                rm = get_max_path_sum(root_node.right)
                root_max = root_node.val + max(0, lm) + max(0, rm)
                lrm = root_node.val + max(0, lm, rm)
                self.max_path_sum = max(self.max_path_sum, max(root_max, lrm))
                return lrm

        get_max_path_sum(root)
        return self.max_path_sum

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Easy
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs_diameter(root_node):
            if root_node is None:
                return -1, -1
            else:
                left_diameter, left_path_len = dfs_diameter(root_node.left)
                right_diameter, right_path_len = dfs_diameter(root_node.right)

                return max(left_diameter, right_diameter, left_path_len + right_path_len + 2), max(left_path_len,
                                                                                                   right_path_len) + 1

        return dfs_diameter(root)[0]
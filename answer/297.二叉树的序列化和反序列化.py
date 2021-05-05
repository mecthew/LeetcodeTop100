from typing import List

# Hard
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        queue = [root]
        ans = ''
        while queue:
            node = queue.pop(0)
            ans += f',{node.val}' if node else f',#'
            if node:
                queue.append(node.left)
                queue.append(node.right)
        return ans


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(',')
        root = None if vals[0] == '#' else TreeNode(int(vals[0]))
        queue = [root] if root else []
        vals.pop(0)
        while queue:
            parent = queue.pop(0)
            left = vals.pop(0)
            right = vals.pop(0)
            left_node = None if left == '#' else TreeNode(int(left))
            right_node = None if right == '#' else TreeNode(int(right))
            parent.left = left_node
            parent.right = right_node
            if left_node:
                queue.append(left_node)
            if right_node:
                queue.append(right_node)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def preorder_dfs(self, root, record_str):
        if not root:
            record_str = record_str + 'null '
        else:
            record_str = record_str + str(root.val) + ' '
            record_str = self.preorder_dfs(root.left, record_str)
            record_str = self.preorder_dfs(root.right, record_str)
        return record_str

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        return self.preorder_dfs(root, "")

    def recover(self, nodes):
        if nodes[0] == 'null':
            nodes.pop(0)
            return None

        root = TreeNode(nodes[0])
        nodes.pop(0)
        root.left = self.recover(nodes)
        root.right = self.recover(nodes)
        return root

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        nodes = data.split(' ')
        root = self.recover(nodes)

        return root



        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.deserialize(codec.serialize(root))
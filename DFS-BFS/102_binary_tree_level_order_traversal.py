# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []

        res = []
        self.nodeAt(root, 0, res)
        return res

    def nodeAt(self, root, level, res):
        if root:
            if len(res) < level + 1: res.append([])
            res[level].append(root.val)
            self.nodeAt(root.left, level + 1, res)
            self.nodeAt(root.right, level + 1, res)







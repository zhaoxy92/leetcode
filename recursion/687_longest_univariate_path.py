# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        self.extendFrom(root)
        return self.ans

    def extendFrom(self, node):
        if node is None: return 0
        left_length = self.extendFrom(node.left)
        right_length = self.extendFrom(node.right)

        left_total = 0
        right_total = 0

        if node.left and node.val == node.left.val:
            left_total = left_length + 1
        if node.right and node.val == node.right.val:
            right_total = right_length + 1

        self.ans = max(self.ans, left_total + right_total)
        return max(left_total, right_total)
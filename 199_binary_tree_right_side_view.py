# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        res = []
        queue = [root]

        while queue:

            res.append(queue[-1].val)

            for _ in range(len(queue)):
                cur = queue.pop(0)
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)

        return res


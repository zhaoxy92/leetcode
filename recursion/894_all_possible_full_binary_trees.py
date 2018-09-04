# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def allFBT(self, n):
        ans = []
        if n % 2 == 0 or n < 1: return []
        if n == 1:
            p = TreeNode(0)
            return [p]

        for i in range(1, n, 2):
            l_trees = self.allFBT(i)
            r_trees = self.allFBT(n - 1 - i)
            for l in l_trees:
                for r in r_trees:
                    p = TreeNode(0)
                    p.left = r
                    p.right = l
                    ans.append(p)
        return ans

    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """

        return self.allFBT(N)



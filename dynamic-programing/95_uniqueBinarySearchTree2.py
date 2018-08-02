# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



def dfs(start, end):

    if start > end:
        return [None]
    res = []
    for i in range(start, end+1):

        left_tree = dfs(start, i-1)
        right_tree = dfs(i+1, end)

        for j in range(len(left_tree)):
            for k in range(len(right_tree)):
                root = TreeNode(i)
                root.left = left_tree[j]
                root.right = right_tree[k]
                res.append(root)
    return res

def generateTrees(n):
    """
    :type n: int
    :rtype: List[TreeNode]
    """
    if n == 0:
        return []

    return dfs(1,n)

print(generateTrees(3))
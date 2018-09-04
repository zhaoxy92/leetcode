class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSameTree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """

    if not len(p) == len(q): return False

    head_p = p[0]
    head_q = q[0]
    if not head_p.val ==head_q.val and isSameTree(head_q.left, head_p.left) and isSameTree(head_p.right, head_q.right):
        return False

    return True



print(isSameTree([1,2,3], [1,2,3]))
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class CBTInserter:

    def __init__(self, root):
        """
        :type root: TreeNode
        """

        todo = []
        cur = root
        q = [cur]
        while q:
            c = q.pop(0)
            if not c.left is None:
                todo.append(c.left.val)
                q.append(c.left)
            if not c.right is None:
                todo.append(c.right.val)
                q.append(c.right)

        self.head = TreeNode(root.val)
        self.queue = [self.head]
        for v in todo:
            self.insert(v)

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """

        cur = TreeNode(v)

        if self.queue[0].left is None:
            self.queue[0].left = cur
        elif self.queue[0].right is None:
            self.queue[0].right = cur
        else:
            self.queue.pop(0)
            self.queue[0].left = cur

        self.queue.append(cur)

        return self.queue[0].val

    def get_root(self):
        """
        :rtype: TreeNode
        """

        return self.head

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
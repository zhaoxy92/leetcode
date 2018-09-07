# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        if head is None: return None

        temp = head
        while temp:
            copy = RandomListNode(temp.label)
            copy.next = temp.next
            temp.next = copy
            temp = temp.next.next

        temp = head
        while temp:
            if temp.random:
                temp.next.random = temp.random.next
            temp = temp.next.next

        pold = head
        head2 = head.next
        pnew = head2

        while pnew.next:
            pold.next = pnew.next
            pold = pold.next
            pnew.next = pold.next
            pnew = pnew.next

        pold.next = None
        pnew.next = None

        return head2

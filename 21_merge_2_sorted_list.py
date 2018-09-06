# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1 is None:
            return l2
        if l2 is None:
            return l1

        p1 = l1
        p2 = l2
        head = None
        if p1.val < p2.val:
            head = p1
            p1 = p1.next
        else:
            head = p2
            p2 = p2.next

        p = head
        while not p1 is None and not p2 is None:
            if p1.val < p2.val:
                p.next = ListNode(p1.val)
                p1 = p1.next
            else:
                p.next = ListNode(p2.val)
                p2 = p2.next
            p = p.next

        if p1 is None:
            p.next = p2
        else:
            p.next = p1

        return head

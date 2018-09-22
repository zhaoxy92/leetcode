# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB: return None
        a = headA
        b = headB
        while a and b and not a == b:
            a = a.next
            b = b.next
            if a == b: return a
            if not a: a = headB
            if not b: b = headA

        return a
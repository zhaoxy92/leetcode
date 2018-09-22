# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head: return True

        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        p = slow.next
        last = None

        while p:
            nx = p.next
            p.next = last
            last = p
            p = nx

        p1 = last
        p2 = head

        same = True
        while p1:
            if not p1.val == p2.val:
                same = False
            p1, p2 = p1.next, p2.next

        return same






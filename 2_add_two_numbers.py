# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1: return l2
        if not l2: return l1

        residual = 0
        ans = ListNode(0)
        cur = ans
        cur_l1 = l1
        cur_l2 = l2

        while cur_l1 or cur_l2:
            v = 0
            if cur_l1 and cur_l2:
                v = cur_l1.val + cur_l2.val + residual
            elif cur_l1:
                v = cur_l1.val + residual
            elif cur_l2:
                v = cur_l2.val + residual

            residual = 1 if v >= 10 else 0
            if v >= 10: v -= 10

            cur.next = ListNode(v)
            cur = cur.next

            if cur_l1: cur_l1 = cur_l1.next
            if cur_l2: cur_l2 = cur_l2.next

        if residual == 1:
            cur.next = ListNode(1)
        return ans.next





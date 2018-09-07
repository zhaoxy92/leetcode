# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        record = {}
        while head:
            if head in record:
                return True
            record[head] = True
            head = head.next

        return False


    def hasCycle(self, head):
        if head == None or head.next == None: return False

        slow = head
        fast = head.next

        while fast != slow:

            if fast == None or fast.next == None:
                return False
            fast = fast.next.next
            slow = slow.next

        return True
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        result = cur = ListNode(0)
        cur.next = head
        while cur.next and cur.next.next:
            p1, p2 = cur.next, cur.next.next
            p1.next = p2.next
            p2.next = p1
            cur = cur.next.next
        return result.next

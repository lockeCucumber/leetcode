# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next == None:
            return []
        length = 1
        node = head
        while node.next != None:
            length += 1
            node = node.next
        nth = length - n
        node = head
        for i in xrange(nth):
            node_before = node
            node = node.next
            node_next = node.next
        node_before.next = node_next
        return head
o = Solution()
head = ListNode(1)
node = ListNode(2)
head.next = node
print head.next.val
print o.removeNthFromEnd(head,1)
print head.next

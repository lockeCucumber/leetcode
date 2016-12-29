# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        lis = []
        while l1:
            lis.append(l1.val)
            l1 = l1.next
        while l2:
            lis.append(l2.val)
            l2 = l2.next
        lis.sort()
        l = ListNode(0)
        result = l
        for i in lis:
            l.next = ListNode(i)
            l = l.next
        return result.next
o = Solution()
a = ListNode(2)
b = ListNode(3)
print o.mergeTwoLists(a,b).next.val

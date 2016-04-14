# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def reverse(self):
        lst = []
        lst.append(self.val)
        var = self.next
        while var != None:
            lst.append(var.val)
            var = var.next
        lst = lst[::-1]
        n = lst[0]
        l_node = ListNode(n)
        for i in lst:
            node = ListNode(i)
            l_node.append(node)
        l_node = l_node.next
        return l_node

    def append(self, node):
        if self.next == None:
            self.next = node
            return
        var = self.next
        while var.next != None:
            var = var.next
        var.next = node
        return

    def length(self):
        var = self
        num = 1
        while var.next != None:
            var = var.next
            num = num + 1
        return num

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # l1 = list_to_lNode(l1)
        # l2 = list_to_lNode(l2)
        
        lst = []
        lst.append(l1.val)
        var = l1.next
        while var != None:
            lst.append(var.val)
            var = var.next
        # lst = lst[::-1]
        n = lst[0]
        l_node = ListNode(n)
        for i in lst:
            node = ListNode(i)
            l_node.append(node)
        l_node = l_node.next
        l1 = l_node
        
        lst = []
        lst.append(l2.val)
        var = l2.next
        while var != None:
            lst.append(var.val)
            var = var.next
        # lst = lst[::-1]
        n = lst[0]
        l_node = ListNode(n)
        for i in lst:
            node = ListNode(i)
            l_node.append(node)
        l_node = l_node.next
        l2 = l_node
        
        # l1 = l1.reverse()
        # l2 = l2.reverse()
        times = min(l1.length(), l2.length())
        l = ListNode(0)
        var1 = l1
        var2 = l2
        for i in range(times):
            node = ListNode(var1.val + var2.val)
            l.append(node)
            var1 = var1.next
            var2 = var2.next
        if var1 != None:
            l.append(var1)
        else:
            l.append(var2)
        l = l.next
        lst = lNode_to_list(l)
        lst_back = lst
        for i in range(len(lst)):
            if lst[i] >= 10 and i < len(lst) - 1:
                lst_back[i+1] = lst_back[i+1] + 1
            if lst[i] >= 10 and i == len(lst) -1:
                lst_back.append(1)
        for i in range(len(lst_back)):
            lst_back[i] = lst_back[i] % 10
        
            
        # lst = []
        # lst.append(l2.val)
        # var = l2.next
        # while var != None:
        #     lst.append(var.val)
        #     var = var.next
        # lst = lst[::-1]
        # n = lst[0]
        # l_node = ListNode(n)
        # for i in lst:
        #     node = ListNode(i)
        #     l_node.append(node)
        # l_node = l_node.next
        # l2 = l_node
        
        return lst_back

def list_to_lNode(lst):
    lNode = ListNode(0)
    for i in lst:
        node = ListNode(i)
        lNode.append(node)
    lNode = lNode.next
    return lNode


def lNode_to_list(lNode):
    lst = []
    lst.append(lNode.val)
    var = lNode.next
    while var != None:
        lst.append(var.val)
        var = var.next
    return lst



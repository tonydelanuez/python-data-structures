# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Create a dummy list node so we can advance one and return the other (one remains at start of list )
        dummy = ListNode(0)
        node = dummy
        while (l1 != None) and (l2 != None):
            if(l1.val < l2.val):
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        node.next = l1 if (l1 != None) else l2
        return dummy.next

test = Solution()
l1 = [1, 5, 6, 7, 10, 19]
l2 = [0, 13, 15, 66, 90]
test.mergeTwoLists(l1, l2)
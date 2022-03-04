# Definition for singly-linked list.
class ListNode:
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        """
        type list1: ListNode
        type list2: ListNode
        rtype: ListNode
        """
        res = ListNode()
        temp = res
        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = ListNode(list1.val)
                temp = temp.next
                list1 = list1.next
            else:
                temp.next = ListNode(list2.val)
                temp = temp.next
                list2 = list2.next
        if list1:
            temp.next = list1
        if list2:
            temp.next = list2
        return res.next
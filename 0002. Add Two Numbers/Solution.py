# Definition for singly-linked list.
class ListNode:
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        type l1: ListNode
        type l2: ListNode
        rtype: ListNode
        """
        res = ListNode()
        temp = res
        carry = 0
        while l1 or l2:
            sum = carry
            if (l1):
                sum += l1.val
                l1 = l1.next
            if (l2):
                sum += l2.val
                l2 = l2.next
            carry = sum // 10
            temp.next = ListNode(sum % 10)
            temp = temp.next
        if carry:
            temp.next = ListNode(carry)
        return res.next
        
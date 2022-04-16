# Definition for singly-linked list.
class ListNode:
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

class Solution:
    def middleNode(self, head):
        """
        type head: ListNode
        rtype: ListNode
        """
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            print(fast.val)
            slow = slow.next
            print(slow.val)
        return slow
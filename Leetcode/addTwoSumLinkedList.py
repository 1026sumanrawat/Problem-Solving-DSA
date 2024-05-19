# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1h = l1
        l2h = l2
        rem = 0
        newlist = ListNode()
        # newlist.head = None
        h = newlist
        while l1h and l2h:

            sums = l1h.val + l2h.val
            if rem != 0:
                sums = sums + rem
            if sums > 9:
                newnode = sums - 10
                rem = 1
            else:
                newnode = sums
                rem = 0

            newlist.next = ListNode(newnode)
            newlist = newlist.next
            l1h = l1h.next
            l2h = l2h.next
        
        
        while l1h:
            
            sums = l1h.val
            if rem != 0:
                sums = sums + rem
            if sums > 9:
                sums = sums - 10
                rem = 1
            else:
                rem = 0
            newlist.next = ListNode(sums)
            newlist = newlist.next
            l1h = l1h.next
        while l2h:
            
            sums = l2h.val
            if rem != 0:
                sums = sums + rem
            if sums > 9:
                sums = sums - 10
                rem = 1
            else:
                rem = 0
            newlist.next = ListNode(sums)
            newlist = newlist.next
            l2h = l2h.next

        if rem != 0:
            newlist.next = ListNode(rem)
        return h.next


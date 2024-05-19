# https://leetcode.com/problems/copy-list-with-random-pointer/submissions/1261705918/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None :
            return None

        curr = head
        while curr:
            temp = curr.next
            new = Node(curr.val)
            new.next = temp
            curr.next = new
            curr = new.next
        node = head
        while node:
            if node.random is not None:
                node.next.random = node.random.next
            node = node.next.next

        node = head
        newHead = head.next
        newcurr = newHead
        while node:
            node.next = newcurr.next
            node = node.next
            if node is not None:
                temp = node.next
                newcurr.next = temp
                newcurr = newcurr.next
        return newHead

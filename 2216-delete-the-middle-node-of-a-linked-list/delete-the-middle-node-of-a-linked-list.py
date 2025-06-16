# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution(object):
    def deleteMiddle(self, head):
        
        # Handling list with 1 node
        if head.next == None:
            return None

        # Calculating length and then finding rth element we need to remove 
        length = 0
        curr = head
        while curr is not None:
            length += 1
            curr = curr.next
        r = int(math.ceil(length / 2.0)) if length % 2 is not 0 else 1 + length / 2
        
        # Traversing to the (r - 1)th element  
        count = 1 
        dummy = head
        while count < r - 1:
            count += 1
            head = head.next

        # If r is last element, set to None, else skip 
        if length == r:
            head.next = None
        else:       
            head.next = head.next.next
        
        return dummy
        
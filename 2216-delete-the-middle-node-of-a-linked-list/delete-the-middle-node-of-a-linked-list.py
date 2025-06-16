# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution(object):
    def deleteMiddle(self, head):
        if head.next == None:
            return None

        length = 0
        curr = head
        while curr is not None:
            length += 1
            curr = curr.next
        
        r = int(math.ceil(length / 2.0)) if length % 2 is not 0 else 1 + length / 2
        count = 1 
        dummy = head
        while count < r - 1:
            count += 1
            head = head.next

        if length == r:
            head.next = None
        else:       
            head.next = head.next.next
        
        return dummy
        
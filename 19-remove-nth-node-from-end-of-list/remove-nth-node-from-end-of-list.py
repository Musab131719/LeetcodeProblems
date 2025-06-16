# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        
        # Finding the rth element from the head that we need to remove
        length = 0
        curr = head
        while curr is not None:
            length += 1
            curr = curr.next
        r = length - n + 1
        
        # Handling if head of linked list needs to be removed
        if r == 1:
            head = head.next
            return head

        # Traversing to the (r-1)th element  
        count = 1
        dummy = head
        while count < r - 1:
            head = head.next
            count += 1

        # If last element needs to be removed, end list. Else, skip the following element 
        if length == r:
            head.next = None
        elif r + 1 <= length:       
            head.next = head.next.next
        
        return dummy

        
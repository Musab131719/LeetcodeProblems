# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        length = 0
        curr = head
        while curr is not None:
            length += 1
            curr = curr.next
        r = length - n + 1
        
        if r == 1:
            head = head.next
            return head

        count = 1
        dummy = head

        while count < r - 1:
            head = head.next
            count += 1

        if length == r:
            head.next = None
        elif r + 1 <= length:       
            head.next = head.next.next
        
        return dummy

        
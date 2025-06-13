# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        current = head
        prev = None
        while current:
            temp = current.next       # Creating a temporary pointer to the remaining linked list 
            current.next = prev       # Changing direction of the arrow 
            prev = current            # Shifting along by 1
            current = temp            # Shifting along by 1
        return prev                

'''prev is the pointer to the previous node during reversal process, and becomes the head of the reversed list'''
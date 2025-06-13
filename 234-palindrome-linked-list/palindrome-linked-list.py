# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        current = head
        A = []
        while current is not None:
            A.append(current.val)
            current = current.next
        return A == A[::-1] 
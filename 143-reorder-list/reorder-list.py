# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):

        # Creating array with elements of linked list
        dummy = head
        A = []
        while dummy is not None:
            A.append(dummy.val)
            dummy = dummy.next

        # Creating a new array with sorted elements
        n = len(A)
        B = [] 
        for i in range(n/2):
            B.append(A[i])
            B.append(A[n-i-1])
        
        # Adjusting for odd midpoint
        if n % 2 is not 0:
            B.append(A[n/2])

        # Changing linked list to match the sorted array
        count = 0
        dummy_2 = head
        while count < n:
            head.val = B[count]
            count += 1
            head = head.next
            
        return dummy_2
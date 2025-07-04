# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        curr1, curr2 = list1, list2
        
        # Checking emptyness
        if curr1 is None:
            return curr2
        if curr2 is None:
            return curr1

        # Initialising head/first value of first node
        list3 = ListNode(min(curr1.val, curr2.val))
        head = list3                                    # Remember the start of list3 so we can return it
        if curr1.val <= curr2.val:
            curr1 = curr1.next
        else:
            curr2 = curr2.next
        
        # Adding values until one of the nodes from list1 and list2 are 'None'
        while curr1 is not None and curr2 is not None:
            if curr1.val <= curr2.val:
                list3.next = ListNode(curr1.val)
                curr1 = curr1.next
            else:
                list3.next = ListNode(curr2.val)
                curr2 = curr2.next
            list3 = list3.next
        
        # Remaining values
        curr_rem = curr1 if curr1 is not None else curr2

        # Adding remaining values
        while curr_rem is not None:
            list3.next = ListNode(curr_rem.val)
            list3 = list3.next
            curr_rem = curr_rem.next
            
        return head
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        dummy = ListNode(0)
        curr = dummy

        l1, l2 = list1, list2

        while l1 and l2:
            
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
                if not l1:
                    curr = curr.next
                    curr.next = l2
            elif l1.val > l2.val:
                curr.next = l2
                l2 = l2.next
                if not l2:
                    curr = curr.next
                    curr.next = l1
            elif l1.val == l2.val:
                curr.next = l1
                l1 = l1.next
                if not l1:
                    curr = curr.next
                    curr.next = l2
                

            curr = curr.next
        return dummy.next
            
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
    
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        prev = None
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        slow.next = None
        l1, l2 = head, prev

        while l1 and l2:
            l1Nn = l1.next
            l2Nn = l2.next

            l1.next = l2
            l2.next = l1Nn

            l1 = l1Nn
            l2 = l2Nn





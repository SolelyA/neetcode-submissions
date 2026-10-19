# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        curr = slow.next
        prev = None
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        slow.next = None
        l1 = head
        l2 = prev

        while l1 and l2:
            l1Nn = l1.next
            l2Nn = l2.next

            l1.next = l2
            l2.next = l1Nn

            l1 = l1Nn
            l2 = l2Nn
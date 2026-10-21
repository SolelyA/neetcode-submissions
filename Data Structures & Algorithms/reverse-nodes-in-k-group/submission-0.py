# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, start: Optional[ListNode], curr: Optional[ListNode]):
        nextNode = curr.next
        curr.next = None
        tail = start
        n = start
        prev = None
        while n:
            nxt = n.next
            n.next = prev
            prev = n
            n = nxt
        tail.next = nextNode
        return prev, tail

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        dummy = ListNode(0)
        dummy.next = head

        start = head

        curr = dummy.next
        count = 0
        prev = dummy

        while curr:
            count += 1
            if count == k:
                newHead, tail = self.reverse(start, curr)
                prev.next = newHead
                start = tail.next
                if tail.next is None:
                    break
                curr = tail.next
                count = 1
                prev = tail
            curr = curr.next
        return dummy.next



        

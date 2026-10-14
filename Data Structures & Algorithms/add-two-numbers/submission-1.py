# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dp = dummy
        tens = 0

        curr1 = l1
        curr2 = l2

        while curr1 or curr2:
            ones = None
            ans = tens
            tens = 0
            if curr1 is not None and curr2 is not None:
                ans += curr1.val + curr2.val
            elif curr1 is None:
                ans += curr2.val
            else:
                ans += curr1.val
            if ans > 9:
                    tens = ans // 10
                    ones = ans % 10
            if ones is not None:
                dp.next = ListNode(ones)
                ones = None
            else:
                dp.next = ListNode(ans)

            if curr1 is not None:
                curr1 = curr1.next
            if curr2 is not None:
                curr2 = curr2.next

            dp = dp.next
        if tens: dp.next = ListNode(tens)

        return dummy.next
        

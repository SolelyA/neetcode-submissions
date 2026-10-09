# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        listLen = 0
        curr = head
        # get the len of the linked list
        while curr:
            listLen += 1
            curr = curr.next

        # get the target index of node to remove
        target = listLen - n

        # init the pointers, make dummy node, set dummy.next to head
        # keep track of last node and current node, remove when target == index
        dummy = ListNode(0)
        dummy.next = head
        node = dummy.next
        prev = dummy
        index = 0
        while node:
            if index == target:
                prev.next = node.next
                break
            prev = node
            index += 1
            node = node.next
        return dummy.next

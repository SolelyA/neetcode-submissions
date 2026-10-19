# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import *
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode(0)
        curr = dummy
        for i, ll in enumerate(lists):
            if ll is not None:
                heappush(heap, (ll.val, i, ll))
        
        while heap:
            val, i, node = heappop(heap)
            if node.next:
                heappush(heap, (node.next.val, i, node.next))
            curr.next = node
            curr = curr.next
        return dummy.next
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        ans = []
        heap = [(-n,i) for i, n in enumerate(nums[left:k], start = left)]
        heapq.heapify(heap)
        ans.append(-heap[0][0])
        for right in range(k, len(nums)):
            heapq.heappush(heap, (-nums[right], right))
            left += 1
            while heap[0][1] < left:
                heapq.heappop(heap)
            ans.append(-heap[0][0])
        return ans
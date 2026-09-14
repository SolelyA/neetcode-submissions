class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        heap = []
        for n in nums:
            if n not in counter:
                counter[n] = 1
            else:
                counter[n] += 1
        
        for key, val in counter.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)
        return [key for val, key in heap]
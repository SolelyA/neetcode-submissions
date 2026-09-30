class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def check(k):
            ans = 0
            for b in piles:
                ans += math.ceil(b/k)
            return ans <= h
        
        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2

            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
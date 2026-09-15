class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = ans = curr = 0

        for right in range(len(prices)):
            if right == left:
                continue
                
            if prices[right] - prices[left] > curr:
                curr = prices[right] - prices[left]
                
            while prices[right] - prices[left] < curr and left != right:
                left += 1
            ans = max(ans, curr)
            curr = 0
        return ans 
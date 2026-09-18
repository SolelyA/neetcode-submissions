class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = ans = 0
        for right in range(len(prices)):
            if right == left:
                continue
            
            if prices[right] - prices[left] > ans:
                ans = prices[right] - prices[left]

            if prices[right] < prices[left]:
                left = right
        return ans
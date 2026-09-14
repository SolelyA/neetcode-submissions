class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        leftMax = 0
        rightMax = 0
        ans = 0
        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])

            if height[right] < height[left]:
                water = rightMax - height[right]
                right -= 1
            else:
                water = leftMax - height[left]
                left += 1
            
            ans += water
        return ans
        
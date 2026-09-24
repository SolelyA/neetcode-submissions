class Solution:
    def trap(self, height: List[int]) -> int:
        left = leftMax = rightMax = water = 0
        right = len(height) - 1

        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])

            if height[right] < height[left]:
                water += rightMax - height[right]
                right -= 1
            else:
                water += leftMax - height[left]
                left += 1
        return water
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = float("-inf")
        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                index, poppedHeight = stack.pop()
                width = i - index
                area = max(area, (width * poppedHeight))
                start = index 
            stack.append((start, height))
        
        while stack:
            index, poppedHeight = stack.pop()
            width = len(heights) - index
            area = max(area, (width * poppedHeight))
        return area
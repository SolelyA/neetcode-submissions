class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0 

        for i, height in enumerate(heights):
            start = i

            while stack and stack[-1][1] > height:
                index, popHeight = stack.pop()
                width = i - index
                area = max(area, popHeight * width)
                start = index
            stack.append((start, height))

        while stack:
            index, height = stack.pop()
            width = len(heights) - index
            area = max(area, height * width)
        return area
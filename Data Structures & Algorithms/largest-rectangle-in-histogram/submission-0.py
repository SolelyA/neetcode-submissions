class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        causeToPop = [0,0]
        area = 0

        for n in range(len(heights)):
            if stack and stack[-1][0] > heights[n]:
                while stack and stack[-1][0] > heights[n]:
                    a = stack.pop()
                    causeToPop[0] = heights[n]
                    causeToPop[1] = a[1]
                    area = max(area, a[0] * (n - a[1]))
                stack.append((heights[n], causeToPop[1]))
            else:
                stack.append((heights[n], n))
        while stack:
            a = stack.pop()
            area = max(area, a[0] * (len(heights) - a[1]))
        return area
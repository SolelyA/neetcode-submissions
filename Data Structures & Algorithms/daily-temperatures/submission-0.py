class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        results = [0] * len(temperatures)

        for i, n in enumerate(temperatures):
            while len(stack) > 0 and stack[-1][0] < n:
                prevTemp = stack.pop()
                results[prevTemp[1]] = i - prevTemp[1]
            stack.append((n,i))
        return results
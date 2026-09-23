class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = float("inf")
    def push(self, val: int) -> None:
        self.stack.append((val, self.minVal))
        self.minVal = min(self.minVal, val)

    def pop(self) -> None:
        if self.stack[-1][0] == self.minVal:
            self.minVal = self.stack[-1][1]
        self.stack.pop()
    
    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        if self.minVal == float("inf"):
            return stack[-1][0]
        else:
            return self.minVal

class TimeMap:

    def __init__(self):
        self.time = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time:
            self.time[key] = []

        self.time[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time:
            return ""
        else:
            tm = self.time[key]
        left = 0
        best = float("-inf")
        right = len(tm) - 1

        while left <= right:
            mid = (left + right) // 2

            if tm[mid][0] <= timestamp:
                best = mid
                left = mid + 1
                
            elif tm[mid][0] > timestamp:
                right = mid - 1
        return self.time[key][best][1] if best > float("-inf") else ""

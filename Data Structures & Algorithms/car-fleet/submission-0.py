class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        stack = []
        cars = []
        for i, x in enumerate(position):
            cars.append((x, speed[i]))
        
        cars.sort(reverse=True)

        for pos, spd in cars:
            time = (target - pos) / spd
            if not stack:
                stack.append(time)
            if time <= stack[-1]:
                continue
            else:
                stack.append(time)
        return len(stack)
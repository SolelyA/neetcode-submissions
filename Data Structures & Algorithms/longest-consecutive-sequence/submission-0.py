class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxCon = 0
        for n in s:
            prev = n - 1
            count = 1
            if prev not in s:
                while n + count in s:
                    count += 1
                maxCon = max(maxCon, count)
        return maxCon


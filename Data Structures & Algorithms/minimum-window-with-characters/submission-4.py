from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        left = 0
        ans = float("inf")
        countT = Counter(t)
        countS = Counter()
        leftIndex = 0
        rightIndex = 0
        need = len(countT)
        have = 0

        for right in range(len(s)):
            countS[s[right]] += 1
            if s[right] in countT and countS[s[right]] == countT[s[right]]:
                have += 1
            while have == need:
                if right - left + 1 < ans:
                    leftIndex = left
                    rightIndex = right
                    ans = right - left + 1
                if s[left] in countT and countS[s[left]] == countT[s[left]]:
                    have -= 1
                countS[s[left]] -= 1
                if countS[s[left]] == 0:
                    del countS[s[left]]
                left += 1
        return "" if ans == float("inf") else s[leftIndex:rightIndex + 1]

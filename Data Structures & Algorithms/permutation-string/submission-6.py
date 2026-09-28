from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        s1Count = Counter(s1)
        s2Count = Counter(s2[0:len(s1)])

        if s1Count == s2Count:
            return True
        
        for right in range(len(s1), len(s2)):
            s2Count[s2[left]] -= 1
            if s2Count[s2[left]] == 0:
                del s2Count[s2[left]]
            left += 1

            s2Count[s2[right]] += 1
            
            if s1Count == s2Count:
                return True
        return False
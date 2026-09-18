from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        left = 0

        s1Count = Counter(s1)
        count = Counter(s2[:len(s1)])

        # Check the first window
        if count == s1Count:
            return True

        for right in range(len(s1), len(s2)):
            # Remove character leaving the window
            count[s2[left]] -= 1

            if count[s2[left]] == 0:
                del count[s2[left]]

            # Add character entering the window
            count[s2[right]] += 1

            left += 1

            # Check the newly formed window
            if count == s1Count:
                return True

        return False
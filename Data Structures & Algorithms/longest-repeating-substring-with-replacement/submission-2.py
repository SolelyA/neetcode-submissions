from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = curr = 0
        seen = defaultdict(int)

        for right in range(len(s)):
            seen[s[right]] += 1

            curr = max(curr, seen[s[right]])

            while (right - left + 1) - curr > k:
                seen[s[left]] -= 1
                if seen[s[left]] == 0:
                    del seen[s[left]]
                left += 1
        return right - left + 1

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = ans = curr = 0
        seen = {}

        for right in range(len(s)):
            if s[right] not in seen:
                seen[s[right]] = 1
            else:
                seen[s[right]] += 1

            curr = max(curr, seen[s[right]])
            while (right - left + 1) - curr > k:
                seen[s[left]] -= 1
                left += 1
        return max(ans, right - left + 1)
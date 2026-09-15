class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = ans = curr = 0
        seen = set()

        for right in range(len(s)):
            if s[right] not in seen:
                seen.add(s[right])
            else:
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1
                seen.add(s[right])
            ans = max(ans, right - left + 1)
        return ans
            
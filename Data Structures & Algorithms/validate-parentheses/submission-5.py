class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
            
        stack = []
        matches = {
            "{" : "}",
            "[" : "]",
            "(" : ")"
        }

        for c in s:
            if c in matches:
                stack.append(c)
            else:
                if not stack:
                    return False
                if matches[stack.pop()] != c:
                    return False
        return not stack
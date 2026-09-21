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
                if stack and matches[stack.pop()] != c:
                    return False
        if stack:
            return False
        return True
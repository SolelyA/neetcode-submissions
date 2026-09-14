class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        book = {}

        if len(s) != len(t):
            return False

        for x in s:
            if x not in book:
                book[x] = 1
            else:
                book[x] += 1
        
        for y in t:
            if y in book:
                book[y] -= 1
            else:
                return False
        
        for kvp in book:
            if book[kvp] >= 1:
                return False
        return True
        
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        book = {}

        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord not in book:
                book[sortedWord] = [word]
            else:
                book[sortedWord].append(word)
        ans = []

        for string in book:
            ans.append(book[string])
        return ans

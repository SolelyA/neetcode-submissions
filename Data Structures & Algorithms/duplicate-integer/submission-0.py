class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        book = set()

        for num in nums:
            if num not in book:
                book.add(num)
            else:
                return True
        return False

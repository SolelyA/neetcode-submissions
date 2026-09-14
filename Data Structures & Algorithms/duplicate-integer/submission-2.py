class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         book = set()

         for n in nums:
            if n not in book:
                book.add(n)
            else:
                return True
         return False
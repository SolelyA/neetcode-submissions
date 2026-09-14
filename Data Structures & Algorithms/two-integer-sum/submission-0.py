class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        book = {}

        for i, n in enumerate(nums):
            ans = target - n
            if ans not in book:
                book[n] = i
            else:
                return [book[ans], i]
        
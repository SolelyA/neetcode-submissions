class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [0] * n
        post = [0] * n

        for i in range(n):
            if i == 0:
                pre[i] = 1
            else:
                pre[i] = nums[i-1] * pre[i-1]
        for i in range(n-1,-1,-1):
            if i == n-1:
                post[i] = 1
            else:
                post[i] = nums[i+1] * post[i+1]
        return [pre[i]*post[i] for i in range(len(pre))]
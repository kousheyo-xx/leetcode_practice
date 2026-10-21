class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n=len(nums)
        preSum=[1]*n
        for i in range(1,n):
            preSum[i]=preSum[i-1]*nums[i-1]
        suffix=1
        for i in range(n-1,-1,-1):
            preSum[i]*=suffix
            suffix*=nums[i]
        return preSum
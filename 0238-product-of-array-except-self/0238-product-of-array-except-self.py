class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n=len(nums)
        prod=[1]*n
        preSum=1
        for i in range(1,n):
            prod[i]=nums[i-1]*prod[i-1]
        suffix=1
        for i in range(n-1,-1,-1):
            prod[i]*=suffix
            suffix*=nums[i]
        return prod
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n=len(nums)
        minProd,maxProd=nums[0],nums[0]
        ans=nums[0]
        for i in range(1,n):
            currMin=minProd
            currMax=maxProd
            minProd=min(nums[i],currMin*nums[i],currMax*nums[i])
            maxProd=max(nums[i],currMax*nums[i],currMin*nums[i])
            ans=max(maxProd,ans)
        return ans
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n=len(nums)
        minProd,maxProd=nums[0],nums[0]
        ans=nums[0]
        for i in range(1,n):
            tempMin=minProd
            tempMax=maxProd
            minProd=min(nums[i],tempMin*nums[i],tempMax*nums[i])
            maxProd=max(nums[i],tempMax*nums[i],tempMin*nums[i])
            ans=max(ans,maxProd)
        return ans
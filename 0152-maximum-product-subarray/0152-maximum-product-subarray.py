class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n=len(nums)
        maxProd,minProd=nums[0],nums[0]
        ans=nums[0]
        for i in range(1,n):
            currMin=minProd
            currMax=maxProd
            maxProd=max(currMax*nums[i],currMin*nums[i],nums[i])
            minProd=min(currMax*nums[i],currMin*nums[i],nums[i])
            ans=max(maxProd,ans)
        return ans
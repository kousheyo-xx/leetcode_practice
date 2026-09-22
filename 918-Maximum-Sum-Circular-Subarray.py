class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        n=len(nums)
        total=sum(nums)
        minSum=nums[0]
        maxSum=nums[0]
        currMin,currMax=nums[0],nums[0]
        for i in range(1,n):
            currMax=max(nums[i],currMax+nums[i])
            currMin=min(nums[i],currMin+nums[i])
            minSum=min(minSum,currMin)
            maxSum=max(maxSum,currMax)
        if maxSum<0:
            return maxSum
        return max(maxSum,total-minSum)
class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        n=len(nums)
        total=sum(nums)
        minSum,maxSum=nums[0],nums[0]
        currMin,currMax=nums[0],nums[0]
        for i in range(1,n):
            currMin=min(nums[i],currMin+nums[i])
            currMax=max(nums[i],currMax+nums[i])
            minSum=min(currMin,minSum)
            maxSum=max(currMax,maxSum)
        if maxSum<0:
            return maxSum
        else:
            return max(maxSum,total-minSum)
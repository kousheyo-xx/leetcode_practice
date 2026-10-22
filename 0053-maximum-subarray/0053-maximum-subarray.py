class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n=len(nums)
        currSum=nums[0]
        maxSum=nums[0]
        for i in range(1,n):
            currSum=max(nums[i],currSum+nums[i])
            maxSum=max(currSum,maxSum)
        return maxSum
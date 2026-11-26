class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n=len(nums)
        currSum,maxSum=float('-inf'),float('-inf')
        for i in range(n):
            currSum=max(currSum+nums[i],nums[i])
            maxSum=max(maxSum,currSum)
        return maxSum
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n=len(nums)
        currSum=float('-inf')
        bestSum=currSum
        for i in range(n):
            currSum=max(currSum+nums[i],nums[i])
            bestSum=max(currSum,bestSum)
        return bestSum
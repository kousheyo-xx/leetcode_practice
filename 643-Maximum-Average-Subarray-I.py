class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        currSum=sum(nums[:k])
        maxSum=currSum
        for i in range(k,n):
            currSum+=nums[i]-nums[i-k]
            maxSum=max(maxSum,currSum)
        return maxSum/k
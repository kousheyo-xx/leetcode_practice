class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        n=len(nums)
        currSum=sum(nums[:k])
        bestSum=currSum
        for i in range(k,n):
            currSum+=nums[i]-nums[i-k]
            bestSum=max(currSum,bestSum)
        return bestSum/k
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        count=0
        preSum={0:1}
        currSum=0
        for i in range(n):
            currSum+=nums[i]
            if currSum-k in preSum:
                count+=preSum[currSum-k]
            preSum[currSum]=preSum.get(currSum,0)+1
        return count
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSum={0:1}
        n=len(nums)
        currSum=0
        count=0
        for i in range(n):
            currSum+=nums[i]
            if currSum-k in preSum:
                count+=preSum[currSum-k]
            preSum[currSum]=preSum.get(currSum,0)+1
        return count
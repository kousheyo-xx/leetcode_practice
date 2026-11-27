class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        n=len(nums)
        preSum={0:1}
        currSum=0
        count=0
        for i in range(n):
            currSum+=nums[i]
            rem=currSum%k
            if rem in preSum:
                count+=preSum[rem]
            preSum[rem]=preSum.get(rem,0)+1
        return count
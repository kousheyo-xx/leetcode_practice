class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        preSum={0:-1}
        n=len(nums)
        currSum=0
        for i in range(n):
            currSum+=nums[i]
            rem=currSum%k
            if rem in preSum:
                if i-preSum[rem]>=2:
                    return True
            else:
                preSum[rem]=i
        return False

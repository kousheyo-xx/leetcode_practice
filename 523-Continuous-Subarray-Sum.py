class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        prefixSum={0:-1}
        n=len(nums)
        currSum=0
        for i in range(n):
            currSum+=nums[i]
            rem=currSum%k
            if rem in prefixSum:
                if i-prefixSum[rem]>=2:
                    return True
            else:
                prefixSum[rem]=i
        return False
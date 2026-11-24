class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        n=len(nums)
        seen={0:-1}
        currSum=0
        for i in range(n):
            currSum+=nums[i]
            rem=currSum%k
            if rem in seen:
                if i-seen[rem]>=2:
                    return True
            else:
                seen[rem]=i
        return False
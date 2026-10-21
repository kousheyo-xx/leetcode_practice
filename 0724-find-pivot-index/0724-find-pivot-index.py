class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        preSum=0
        sufSum=sum(nums)
        n=len(nums)
        for i in range(n):
            sufSum-=nums[i]
            if preSum==sufSum:
                return i
            preSum+=nums[i]
        return -1
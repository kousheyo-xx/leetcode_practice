class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        preArray=[1]*n
        prefix=1
        for i in range(n):
            preArray[i]=prefix
            prefix*=nums[i]
        suffix=1
        for i in range(n-1,-1,-1):
            preArray[i]*=suffix
            suffix=suffix*nums[i]
        return preArray




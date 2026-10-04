class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n=len(nums)
        i=0
        while i<n:
            if nums[i]>0:
                correct=nums[i]-1
                if correct<n and nums[correct]!=nums[i]:
                    nums[correct],nums[i]=nums[i],nums[correct]
                else:
                    i+=1
            else:
                i+=1
        for i in range(n):
            if nums[i]!=i+1:
                return i+1
        return n+1
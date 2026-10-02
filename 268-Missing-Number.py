class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        i=0
        while i<n:
            correct=nums[i]
            if correct<n and i!=correct:
                nums[correct],nums[i]=nums[i],nums[correct]
            else:
                i+=1
        for i in range(n):
            if nums[i]!=i:
                return i
        return n
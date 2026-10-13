class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        i=0
        for j in range(n):
            if nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
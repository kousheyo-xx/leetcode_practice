class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        i=1
        for j in range(2,n):
            if nums[j]!=nums[i-1]:
                i+=1
                nums[i]=nums[j]
        return i+1
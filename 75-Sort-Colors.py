class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        i,j,k=0,0,n-1
        while j<=k:
            if nums[j]==0:
                nums[j],nums[i]=nums[i],nums[j]
                i+=1
                j+=1
            elif nums[j]==1:
                j+=1
            else:
                nums[j],nums[k]=nums[k],nums[j]
                k-=1
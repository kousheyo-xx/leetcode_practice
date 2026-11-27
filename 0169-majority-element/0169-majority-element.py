class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n=len(nums)
        candidate=nums[0]
        count=0
        for i in range(n):
            if count==0:
                candidate=nums[i]
            if nums[i]==candidate:
                count+=1
            else:
                count-=1
        return candidate
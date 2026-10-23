class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n=len(nums)
        candidate=nums[0]
        count=0
        for num in nums:
            if count==0:
                candidate=num
            if num==candidate:
                count+=1
            else:
                count-=1
        count=0
        for num in nums:
            if num==candidate:
                count+=1
        if count>=n//2:
            return candidate
        return -1
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n=len(nums)
        candidate=nums[0]
        count=0
        for num in nums:
            if count==0:
                candidate=num
                count=0
            if num==candidate:
                count+=1
            else:
                count-=1
        return candidate
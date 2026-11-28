class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums=set(nums)
        ans=0
        for num in nums:
            if num-1 not in nums:
                elm=num
                curr=0
                while elm in nums:
                    curr+=1
                    elm+=1
                ans=max(ans,curr)
        return ans
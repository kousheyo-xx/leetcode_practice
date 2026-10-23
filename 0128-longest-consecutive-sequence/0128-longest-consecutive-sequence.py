class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums=set(nums)
        currLen,maxLen=0,0
        for num in nums:
            elm=num
            currLen=0
            if elm-1 not in nums:
                while elm in nums:
                    currLen+=1
                    elm+=1  
            maxLen=max(maxLen,currLen)
        return maxLen
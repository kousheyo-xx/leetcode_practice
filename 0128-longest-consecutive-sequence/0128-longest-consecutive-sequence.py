class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        seen=set(nums)
        n=len(nums)
        maxLen=0
        for num in seen:
            elm=num
            if elm-1 not in seen:
                currLen=0
                while elm in seen:
                    currLen+=1
                    elm+=1
                maxLen=max(currLen,maxLen)
        return maxLen

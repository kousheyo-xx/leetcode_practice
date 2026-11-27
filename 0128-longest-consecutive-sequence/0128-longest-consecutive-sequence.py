class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        seen=set(nums)
        n=len(nums)
        maxLen=0
        for num in seen:
            elm=num
            if num-1 not in seen:
                currLen=0
                while num in seen:
                    currLen+=1
                    num+=1
                maxLen=max(currLen,maxLen)
        return maxLen

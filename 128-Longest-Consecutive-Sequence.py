class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums=set(nums)
        longest=0
        n=len(nums)
        for num in nums:
            elm=num
            curr=0
            if elm-1 not in nums:
                while elm in nums:
                    curr+=1
                    elm+=1
            longest=max(longest,curr)
        return longest
            
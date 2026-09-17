class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        zeroCount=0
        n=len(nums)
        left=0
        ans=0
        for right in range(n):
            if nums[right]==0:
                zeroCount+=1
            while zeroCount>k:
                if nums[left]==0:
                    zeroCount-=1
                left+=1
            ans=max(ans,right-left+1)
        return ans
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left=0
        n=len(nums)
        currSum=0
        ans=float('inf')
        for right in range(n):
            currSum+=nums[right]
            while currSum>=target:
                ans=min(ans,right-left+1)
                currSum-=nums[left]
                left+=1
        return ans if ans!=float('inf') else 0
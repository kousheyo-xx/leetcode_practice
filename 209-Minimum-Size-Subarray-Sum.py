class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        ans=float('inf')
        n=len(nums)
        left=0
        currSum=0
        for right in range(n):
            currSum+=nums[right]
            while currSum>=target:
                ans=min(ans,right-left+1)
                currSum-=nums[left]
                left+=1
        return ans if ans!=float('inf') else 0
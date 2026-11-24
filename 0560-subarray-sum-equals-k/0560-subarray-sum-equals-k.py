class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen={0:1}
        n=len(nums)
        count=0
        currSum=0
        for i in range(n):
            currSum+=nums[i]
            if currSum-k in seen:
                count+=seen[currSum-k]
            seen[currSum]=seen.get(currSum,0)+1
        return count
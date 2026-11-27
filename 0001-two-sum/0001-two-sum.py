class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n=len(nums)
        seen={}
        for i in range(n):
            if target-nums[i] in seen:
                return [seen[target-nums[i]],i]
            seen[nums[i]]=i
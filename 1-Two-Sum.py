class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen={}
        n=len(nums)
        for i in range(n):
            if target-nums[i] in seen:
                return [seen[target-nums[i]],i]
            seen[nums[i]]=i
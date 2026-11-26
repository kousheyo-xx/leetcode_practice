class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        suffix=sum(nums)
        prefix=0
        n=len(nums)
        for i in range(n):
            suffix-=nums[i]
            if suffix==prefix:
                return i
            prefix+=nums[i]
        return -1
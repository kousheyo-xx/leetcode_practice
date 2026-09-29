class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        bestSum=nums[0]+nums[1]+nums[2]
        for i in range(n-2):
            if nums[i]==nums[i-1]:
                continue
            j=i+1
            k=n-1
            while j<k:
                currSum=nums[i]+nums[j]+nums[k]
                if currSum==target:
                    return currSum
                if abs(currSum-target)<abs(bestSum-target):
                    bestSum=currSum
                if currSum<target:
                    j+=1
                else:
                    k-=1
        return bestSum
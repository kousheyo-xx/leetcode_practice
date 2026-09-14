class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n=len(nums)
        nums.sort()
        bestSum=nums[0]+nums[1]+nums[2]
        currSum=0
        for i in range(n-2):
            j=i+1
            k=n-1
            while j<k:
                currSum=nums[i]+nums[j]+nums[k]
                if currSum==target:
                    return currSum
                elif abs(currSum-target)<abs(bestSum-target):
                    bestSum=currSum
                if currSum<target:
                    j+=1
                else:
                    k-=1
        return bestSum


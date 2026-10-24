class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        bestSum=nums[0]+nums[1]+nums[2]
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=n-1
            while j<k:
                if nums[i]+nums[j]+nums[k]==target:
                    return target
                if abs(target-(nums[i]+nums[j]+nums[k]))<abs(target-bestSum):
                    bestSum=nums[i]+nums[j]+nums[k]
                if nums[i]+nums[j]+nums[k]<target:
                    j+=1
                else:
                    k-=1
        return bestSum
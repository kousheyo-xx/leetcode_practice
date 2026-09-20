class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        freq={0:1}
        n=len(nums)
        currSum=0
        count=0
        for i in range(n):
            currSum+=nums[i]
            rem=currSum%k
            if rem in freq:
                count+=freq[rem]
            freq[rem]=freq.get(rem,0)+1
        return count
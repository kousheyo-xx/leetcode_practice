class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        threshold*=k
        n=len(arr)
        currSum=sum(arr[:k])
        count=0
        if currSum>=threshold:
            count+=1
        for i in range(k,n):
            currSum+=arr[i]-arr[i-k]
            if currSum>=threshold:
                count+=1
        return count
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count=0
        n=len(arr)
        threshold*=k
        currSum=sum(arr[:k])
        if currSum>=threshold:
            count+=1
        for i in range(k,n):
            currSum+=arr[i]-arr[i-k]
            if currSum>=threshold:
                count+=1
        return count
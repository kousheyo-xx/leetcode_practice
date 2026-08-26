class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold*=k
        n=len(arr)
        currSum=sum(arr[:k])
        c=0
        if currSum>=threshold:
            c+=1
        for i in range(k,n):
            currSum+=arr[i]-arr[i-k]
            if currSum>=threshold:
                c+=1
        return c
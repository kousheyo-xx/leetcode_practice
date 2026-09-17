class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq={}
        maxFreq=0
        n=len(s)
        left=0
        ans=0
        for right in range(n):
            freq[s[right]]=freq.get(s[right],0)+1
            maxFreq=max(maxFreq,freq[s[right]])
            while right-left+1-maxFreq>k:
                freq[s[left]]-=1
                left+=1
            ans=max(ans,right-left+1)
        return ans



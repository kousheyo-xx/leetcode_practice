class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mpp={}
        n=len(s)
        ans=0
        maxFreq=0
        left=0
        for right in range(n):
            mpp[s[right]]=mpp.get(s[right],0)+1
            maxFreq=max(maxFreq,mpp[s[right]])
            while right-left+1-maxFreq>k:
                mpp[s[left]]-=1
                left+=1
            ans=max(right-left+1,ans)
        return ans
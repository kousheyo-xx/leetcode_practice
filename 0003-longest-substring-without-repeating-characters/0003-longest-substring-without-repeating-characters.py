class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        n=len(s)
        left=0
        ans=0
        for right in range(n):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            ans=max(ans,right-left+1)
        return ans
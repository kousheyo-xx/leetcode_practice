class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        ans=0
        left=0
        n=len(s)
        for right in range(n):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            ans=max(ans,right-left+1)
        return ans

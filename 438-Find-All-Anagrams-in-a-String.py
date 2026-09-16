class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        lenP=len(p)
        lenS=len(s)
        if lenP>lenS:
            return []
        ans=[]
        pMap={}
        for ch in p:
            pMap[ch]=pMap.get(ch,0)+1
        sMap={}
        for i in range(lenP):
            sMap[s[i]]=sMap.get(s[i],0)+1
        if sMap==pMap:
            ans.append(0)
        for i in range(lenP,lenS):
            sMap[s[i]]=sMap.get(s[i],0)+1
            sMap[s[i-lenP]]-=1
            if sMap[s[i-lenP]]==0:
                del(sMap[s[i-lenP]])
            if sMap==pMap:
                ans.append(i-lenP+1)
        return ans
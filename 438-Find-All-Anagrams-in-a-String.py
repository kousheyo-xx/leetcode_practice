class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s=len(s)
        len_p=len(p)
        if len_p>len_s:
            return []
        pMap={}
        for ch in p:
            pMap[ch]=pMap.get(ch,0)+1
        res=[]
        sMap={}
        for i in range(len_p):
            sMap[s[i]]=sMap.get(s[i],0)+1
        if sMap==pMap:
            res.append(0)
        for i in range(len_p,len_s):
            sMap[s[i]]=sMap.get(s[i],0)+1
            sMap[s[i-len_p]]-=1
            if sMap[s[i-len_p]]==0:
                del(sMap[s[i-len_p]])
            if sMap==pMap:
                res.append(i-len_p+1)
        return res
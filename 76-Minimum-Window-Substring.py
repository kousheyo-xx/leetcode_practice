class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lenT=len(t)
        lenS=len(s)
        if lenT>lenS:
            return ""
        ansLen=float('inf')
        l,r=0,0
        left=0
        tMap={}
        for ch in t:
            tMap[ch]=tMap.get(ch,0)+1
        need=len(tMap)
        have=0
        sMap={}
        for right in range(lenS):
            sMap[s[right]]=sMap.get(s[right],0)+1
            if s[right] in tMap and sMap[s[right]]==tMap[s[right]]:
                    have+=1
            while have==need:
                if ansLen>right-left+1:
                    l=left
                    r=right
                    ansLen=right-left+1
                sMap[s[left]]-=1
                if s[left] in tMap and sMap[s[left]]<tMap[s[left]]:
                    have-=1
                left+=1                    
        return s[l:r+1] if ansLen!=float('inf') else ""

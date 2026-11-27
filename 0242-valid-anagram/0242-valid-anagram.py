class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t)!=len(s):
            return False
        tMap={}
        for ch in t:
            tMap[ch]=tMap.get(ch,0)+1
        sMap={}
        for ch in s:
            sMap[ch]=sMap.get(ch,0)+1
        return sMap==tMap
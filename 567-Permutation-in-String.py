class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lenS1=len(s1)
        lenS2=len(s2)
        if lenS1>lenS2:
            return False
        s1Map={}
        for ch in s1:
            s1Map[ch]=s1Map.get(ch,0)+1
        s2Map={}
        for i in range(lenS1):
            s2Map[s2[i]]=s2Map.get(s2[i],0)+1
        if s1Map==s2Map:
            return True
        for i in range(lenS1,lenS2):
            s2Map[s2[i]]=s2Map.get(s2[i],0)+1
            s2Map[s2[i-lenS1]]-=1
            if s2Map[s2[i-lenS1]]==0:
                del(s2Map[s2[i-lenS1]])
            if s1Map==s2Map:
                return True
        return False
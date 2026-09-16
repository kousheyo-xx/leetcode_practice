class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lens1=len(s1)
        lens2=len(s2)
        if lens1>lens2:
            return False
        s1Map={}
        for ch in s1:
            s1Map[ch]=s1Map.get(ch,0)+1
        s2Map={}
        for i in range(lens1):
            s2Map[s2[i]]=s2Map.get(s2[i],0)+1
        if s2Map==s1Map:
            return True
        for i in range(lens1,lens2):
            s2Map[s2[i]]=s2Map.get(s2[i],0)+1
            s2Map[s2[i-lens1]]-=1
            if s2Map[s2[i-lens1]]==0:
                del(s2Map[s2[i-lens1]])
            if s2Map==s1Map:
                return True
        return False
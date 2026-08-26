class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1=len(s1)
        len_s2=len(s2)
        if len_s1>len_s2:
            return False
        s1Map={}
        for ch in s1:
            s1Map[ch]=s1Map.get(ch,0)+1
        s2Map={}
        for i in range(len_s1):
            s2Map[s2[i]]=s2Map.get(s2[i],0)+1
        if s1Map==s2Map:
            return True
        for i in range(len_s1,len_s2):
            s2Map[s2[i]]=s2Map.get(s2[i],0)+1
            s2Map[s2[i-len_s1]]-=1
            if s2Map[s2[i-len_s1]]==0:
                del(s2Map[s2[i-len_s1]])
            if s1Map==s2Map:
                return True
        return False
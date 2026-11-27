class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        grp={}
        for word in strs:
            key="".join(sorted(word))
            if key in grp:
                grp[key].append(word)
            else:
                grp[key]=[]
                grp[key].append(word)
        res=[]
        for key in grp:
            res.append(grp[key])
        return res
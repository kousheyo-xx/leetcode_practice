class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups={}
        res=[]
        n=len(strs)
        for i in range(n):
            word="".join(sorted(strs[i]))
            if word in groups:
                groups[word].append(strs[i])
            else:
                groups[word]=[strs[i]]
        for word in groups:
            res.append(groups[word])
        return res
        
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams={}
        for word in strs:
            key="".join(sorted(word))
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key]=[]
                anagrams[key].append(word)
        res=[]
        for key in anagrams:
            res.append(anagrams[key])
        return res
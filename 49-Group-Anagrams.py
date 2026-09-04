class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams={}
        res=[]
        for word in strs:
            key="".join(sorted(word))
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key]=[word]
        for word in anagrams:
            res.append(anagrams[word])
        return res
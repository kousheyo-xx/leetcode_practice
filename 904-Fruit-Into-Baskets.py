class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        n=len(fruits)
        left=0
        fruitMap={}
        ans=0
        for right in range(n):
            fruitMap[fruits[right]]=fruitMap.get(fruits[right],0)+1
            while len(fruitMap)>2:
                fruitMap[fruits[left]]-=1
                if fruitMap[fruits[left]]==0:
                    del(fruitMap[fruits[left]])
                left+=1
            ans=max(ans,right-left+1)
        return ans

class Solution:
    def maxArea(self, height: list[int]) -> int:
        i,j=0,len(height)-1
        water=0
        maxWater=0
        while i<j:
            water=(j-i)*min(height[i],height[j])
            maxWater=max(water,maxWater)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return maxWater
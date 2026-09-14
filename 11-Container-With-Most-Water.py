class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j=0,len(height)-1
        maxArea,area=0,0
        while i<=j:
            area=min(height[i],height[j])*(j-i)
            maxArea=max(area,maxArea)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return maxArea
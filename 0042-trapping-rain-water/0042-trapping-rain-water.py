class Solution:
    def trap(self, height: list[int]) -> int:
        i,j=0,len(height)-1
        maxRight,maxLeft=height[j],height[i]
        water=0
        while i<=j:
            if height[i]<height[j]:
                maxLeft=max(maxLeft,height[i])
                water+=maxLeft-height[i]
                i+=1
            else:
                maxRight=max(maxRight,height[j])
                water+=maxRight-height[j]
                j-=1
        return water
class Solution:
    def trap(self, height: List[int]) -> int:
        i,j=0,len(height)-1
        water=0
        maxLeft,maxRight=height[i],height[j]
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
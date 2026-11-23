class Solution:
    def trap(self, height: list[int]) -> int:
        i,j=0,len(height)-1
        leftMax,rightMax=height[i],height[j]
        water=0
        while i<=j:
            if height[i]<height[j]:
                leftMax=max(height[i],leftMax)
                water+=leftMax-height[i]
                i+=1
            else:
                rightMax=max(height[j],rightMax)
                water+=rightMax-height[j]
                j-=1
        return water
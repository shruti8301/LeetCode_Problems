class Solution:
    def trap(self, height: List[int]) -> int:
        mxl=[0]*len(height)
        mxr=[0]*len(height)
        mxl[0]=height[0]
        for i in range(1,len(height)):
            mxl[i]=max(mxl[i-1],height[i])
        mxr[len(height)-1]=height[len(height)-1]
        for i in range(len(height)-2,-1,-1):
            mxr[i]=max(mxr[i+1],height[i])
        water=0
        for i in range(len(height)):
            water+=min(mxl[i],mxr[i])-height[i]
        return (water)
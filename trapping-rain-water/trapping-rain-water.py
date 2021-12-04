class Solution:
    def trap(self, height: List[int]) -> int:
        area=0
        maxl=0
        maxr=0
        l=0
        r=len(height)-1
        while l<r:
            if height[l]<height[r]:
                if height[l]>maxl:
                    maxl=height[l]
                else:
                    area+=maxl-height[l]
                l+=1
            else:
                if height[r]>maxr:
                    maxr=height[r]
                else:
                    area+=maxr-height[r]
                r-=1
                
        return area
        
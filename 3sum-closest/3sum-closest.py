import sys
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if nums is None or len(nums)<3:
            return
        nums.sort()
        result=0
        minimum=sys.maxsize
        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1
            while j<k:
                sumt=nums[i]+nums[j]+nums[k]
                diff=abs(sumt-target)
                if diff==0:
                    return sumt
                if diff<minimum:
                    minimum=diff
                    result=sumt
            
                if sumt<target:
                    j+=1
                else:
                    k-=1
        return result
                
            
            
        
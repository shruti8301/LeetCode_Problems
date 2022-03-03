class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        cdiff=-1
        c=0
        r=0
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]!=cdiff:
                c=1
                cdiff=nums[i]-nums[i-1]
            else:
                r+=c

                c+=1
                
        return r
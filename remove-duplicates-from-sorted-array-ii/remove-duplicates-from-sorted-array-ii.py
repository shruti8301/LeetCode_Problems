class Solution:
    def removeDuplicates(self, nums: List[int]):
        l=0
        last=None
        c=0
        for r in range(len(nums)):
            if nums[r]!=last:
                nums[l]=nums[r]
                l+=1
                last=nums[r]
                c=1
            elif c<2:
                nums[l]=nums[r]
                l+=1
                c+=1
        return l
   
            
    
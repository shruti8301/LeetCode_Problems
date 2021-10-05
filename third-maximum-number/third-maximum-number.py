class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=set(nums)
        nums=list(nums)
        a=[]
        while nums:
            a.append(max(nums))
            nums.remove(max(nums))
        if len(a)==2:
            return a[0]
        elif len(a)==1:
            return a[0]
        else:
            return a[2]
        
                
        
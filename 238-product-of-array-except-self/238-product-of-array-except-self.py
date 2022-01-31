import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a=nums[0]
        r=[1]*len(nums)
        for i in range(1,len(nums)):
            r[i]=a
            a*=nums[i]
        a=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            r[i]*=a
            a*=nums[i]
        return r
        
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        r=nums[0]
        minnums=nums[0]
        maxnums=nums[0]
        for i in range(1,len(nums)):
            temp=minnums
            minnums=min(nums[i],nums[i]*minnums,nums[i]*maxnums)
            maxnums=max(nums[i],nums[i]*maxnums,nums[i]*temp)
            r=max(r,maxnums)
        return r
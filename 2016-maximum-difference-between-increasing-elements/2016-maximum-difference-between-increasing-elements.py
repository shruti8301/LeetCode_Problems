class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mn=nums[0]
        diff=-1
        for i in range(1,len(nums)):
            if nums[i]<mn:
                mn=nums[i]
            elif nums[i]>mn:
                diff=max(diff,nums[i]-mn)
        return diff
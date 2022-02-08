class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        l=0
        r=len(nums)-1
        if nums[-1]>nums[0]:
            return nums[0]
        while l<=r:
            mid=(l+r)//2
            if nums[mid+1]<nums[mid]:
                return nums[mid+1]
            if nums[mid]<nums[mid-1]:
                return nums[mid]
            if nums[mid]>nums[0]:
                l=mid+1
            else:
                r=mid-1
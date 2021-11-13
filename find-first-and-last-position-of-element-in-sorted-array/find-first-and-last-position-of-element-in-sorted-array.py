class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=len(nums)-1
        f,e=-1,-1
        #rightpart
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                f=mid
                r=mid-1
            elif target<nums[mid]:
                r=mid-1
            elif target>nums[mid]:
                l=mid+1
        #leftpart    
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                e=mid
                l=mid+1
            elif target<nums[mid]:
                r=mid-1
            elif target>nums[mid]:
                l=mid+1
        return [f,e]
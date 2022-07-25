class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                break
            if nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
        if l>r:
            return [-1,-1]
        start=end=mid
        while start>=0 and nums[start]==target:
            start-=1
        while end<len(nums) and nums[end]==target:
            end+=1
        return [start+1,end-1]
                
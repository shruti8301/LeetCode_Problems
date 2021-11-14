class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        r=len(nums)-1
        mid=0
        while mid<=r:
            if nums[mid]==0:
                nums[l],nums[mid]=nums[mid],nums[l]
                mid+=1
                l+=1
            elif nums[mid]==2:
                nums[r],nums[mid]=nums[mid],nums[r]
                r-=1
            else:
                mid+=1
        return nums
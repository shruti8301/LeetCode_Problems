class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i=n-1
        while i>0 and nums[i-1]>=nums[i]:
            i-=1
        if i==0:
            return nums.reverse()
        k=i-1
        j=n-1
        while nums[j] <= nums[k]:
            j-=1
        nums[j], nums[k] = nums[k], nums[j]
        # Reverse the elements from k+1 till end
        l, r = k+1, n-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1
            
        
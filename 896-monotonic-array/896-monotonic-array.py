class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        a=sorted(nums)
        if a==nums or a==nums[::-1]:
            return True
        
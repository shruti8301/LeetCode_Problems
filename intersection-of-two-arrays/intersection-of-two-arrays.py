class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(set(nums1).intersection(set(nums2)))>0:
            return set(nums1).intersection(set(nums2))
        
        
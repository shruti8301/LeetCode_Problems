from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a=Counter(nums)
        for key in a:
            if a[key]==1:
                return key
            
            
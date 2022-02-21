from collections import Counter
import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a=Counter(nums)
        for i in a:
            if a[i]>math.floor(len(nums)/2):
                return i
        
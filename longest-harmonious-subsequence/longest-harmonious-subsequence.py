from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        c=Counter(nums)
        a=0
        for i in c:
            if i+1 in c and (c[i]+c[i+1])>a:
                a=c[i]+c[i+1]
        return a
                
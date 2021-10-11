class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        g=0
        for i in range(len(nums)):
            if nums[i]==1:
                c+=1
                g=max(g,c)
            else:
                c=0
        return g

        
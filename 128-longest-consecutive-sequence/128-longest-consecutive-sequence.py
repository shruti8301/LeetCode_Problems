class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        maxc=1
        i=1
        c=1
        for i in range(len(nums)):
            print(nums[i])
            if nums[i]!=nums[i-1]:
                if nums[i]-nums[i-1]==1:
                   # i+=1
                    c+=1
                    maxc=max(maxc,c)
                else:
                    #i+=1
                    c=1
                    #maxc=max(maxc,c)
        return(max(c,maxc))
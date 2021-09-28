class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i=j=0
        ans=[]
        while j<len(nums):
            while j<len(nums)-1 and nums[j]+1==nums[j+1]:
                j+=1
            ans.append(str(nums[i])+"->"+str(nums[j]) if i!=j else str(nums[i]))
            i=j=j+1
        return ans
        
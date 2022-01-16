class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1:
            return [nums]
        if len(nums)==2:
            return [[nums[0],nums[1]],[nums[1],nums[0]]]
        result=[]
        for i in range(len(nums)):
            numscopy=nums.copy()
            value=numscopy.pop(i)
            a=self.permute(numscopy)
            for j in range(len(a)):
                result.append([value]+a[j])
        return result
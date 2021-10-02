class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr=[]
        for i in range(0,len(nums)+1):
            arr.append(i)

        if len(nums)!=len(arr):
            n= list(set(arr) - set(nums))
            return n[0]
        
        
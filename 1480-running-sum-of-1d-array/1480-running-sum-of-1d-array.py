class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        suma=0
        
        i=0
        while i<len(nums):
            suma+=nums[i]
            #print(suma)
            nums[i]=suma
            i+=1
        return nums
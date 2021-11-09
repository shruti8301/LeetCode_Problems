class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        arr=[]
        arr2=[]
        for i in nums:
            if i not in arr:
                arr.append(i)
            else:
                arr2.append(i)
        arr3=[]
        for i in range(1,len(nums)+1):
            arr3.append(i)
        miss=set(arr3)-set(nums)
        arr2=arr2+list(miss)        
        return arr2
        
        
        
        
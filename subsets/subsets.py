class Solution:
    def subsets(self, nums):
        arr=[[]]
        for i in nums:
            arr+=[j +[i] for j in arr]
        return arr
           
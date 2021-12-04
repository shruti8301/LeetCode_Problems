class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_set=set(nums)
        arr=[]
        for i in range(1,len(nums)+2):
            if i not in nums_set:
                arr.append(i)
        return min(arr)
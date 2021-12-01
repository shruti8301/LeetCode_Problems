import itertools
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=set()
        def dfs(index=0,arr=[]):
            for i in range(index,len(nums)+1):
                if i==len(nums):
                    res.add(tuple(arr))
                    return 
                dfs(i+1,arr+[nums[i]])
        dfs()
        return res
            
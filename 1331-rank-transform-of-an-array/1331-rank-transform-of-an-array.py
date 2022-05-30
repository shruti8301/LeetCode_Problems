class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d={}
        nums=sorted(list(set(arr)))
        for i in range(len(nums)):
            d[nums[i]]=i+1
        return [d[i] for i in arr]
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        arr=sorted(nums)
        if len(arr)==1:
            return 0
        elif len(arr)>=2 and arr[-1]>=2*arr[-2]:
            return nums.index(arr[-1])
        else:
            return -1
        
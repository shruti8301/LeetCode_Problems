import sys
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mn=sys.maxsize
        nums=[]
        for i in range(len(arr)-1):
            mn=min(mn,arr[i+1]-arr[i])
        for i in range(len(arr)-1):
            if mn==(arr[i+1]-arr[i]):
                nums.append([arr[i],arr[i+1]])
        return nums
            
import heapq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #we will use heap here
        heapify(nums)
        arr=[]
        for i in range(len(nums)):
            arr.append(nums[0])
            heappop(nums)
        return(arr)
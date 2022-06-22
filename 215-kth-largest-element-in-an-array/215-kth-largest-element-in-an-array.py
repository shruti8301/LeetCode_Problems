import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr=[]
        #ans=-1
        for i in nums:
            heapify(arr)
            heappush(arr,-1*i)
            
        while k:
            ans=-1*heappop(arr)
            k-=1
        return ans
            
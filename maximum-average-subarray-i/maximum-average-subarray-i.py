class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
       
        total=sum(nums[0:k])
        maxn=total

        for i in range(len(nums)-k):
            total-=nums[i]
            total+=nums[i+k]
            maxn=max(maxn,total)
        return maxn/k
        
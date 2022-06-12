class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        arr=set()
        curr_sum=0
        max_sum=0
        l=0
        for i in nums:
            while i in arr:
                curr_sum-=nums[l]
                arr.remove(nums[l])
                l+=1
            curr_sum+=i
            arr.add(i)
            max_sum=max(max_sum,curr_sum)
        return max_sum
            
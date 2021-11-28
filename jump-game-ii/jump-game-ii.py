class Solution:
    def jump(self, nums: List[int]) -> int:
        end=farthest=0
        total_steps=0
        for i in range(0,len(nums)-1):
            farthest=max(farthest,nums[i]+i)
            if i==end:
                end=farthest
                total_steps+=1
        return total_steps
        
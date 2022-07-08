class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m=0
        for i in range(len(nums)-1):
            if i<=m:
                m=max(m,i+nums[i])
        return m>=len(nums)-1
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i + nums[i]>=last:
                last=i
        if last==0:
            return True
        else:
            return False
class Solution:
    def subsetsum(self, nums, sum):
        dp = [[0 for j in range(sum+1)] for i in range(len(nums)+1)]
        for i in range(len(nums)+1):
            dp[i][0] = 1
        for i in range(1, len(nums)+1):
            for j in range(sum+1):
                if nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[len(nums)][sum]
    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        diffsum = sum(nums) - target
        if diffsum < 0:
            return 0
        if diffsum%2 != 0:
            return 0
        return self.subsetsum(nums, diffsum//2)
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        def knapsack(items, max_weight):
            dp = [[0 for i in range(max_weight+1)] for j in range(len(items))]
            for i,item in enumerate(items):
                for weight in range(max_weight+1):
                    if item <= weight:
                        dp[i][weight] = max(dp[i-1][weight], dp[i-1][weight-item]+item)
                    else:
                        dp[i][weight] = dp[i-1][weight]
            return dp[-1][-1]
			
        s = sum(stones)
        return s - 2*knapsack(stones,s//2)
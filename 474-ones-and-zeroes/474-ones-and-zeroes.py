from collections import Counter
class Solution:
    def findMaxForm(self, strs, m, n):
        dp = [[0]*(n+1) for _ in range(m+1)]
        dict1 = [[i.count("0"), i.count("1")] for i in strs]

        for zeroes, ones in dict1:
            for i in reversed(range(zeroes, m+1)):
                for j in reversed(range(ones, n+1)):
                    dp[i][j] = max(dp[i][j], 1 + dp[i-zeroes][j-ones])


        return dp[-1][-1]
        
            
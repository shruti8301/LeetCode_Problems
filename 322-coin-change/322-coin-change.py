import sys
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        t=[[0 for x in range(amount+1)] for x in range(len(coins)+1)]
        for i in range(len(coins)+1):
            for j in range(amount+1):
                t[0][j]=sys.maxsize-1
                t[i][0]=0
        for i in range(len(coins)+1):
            for j in range(amount+1):
                if j%coins[0]==0:
                    t[i][j]=j//coins[0]
                else:
                    t[i][j]=sys.maxsize-1
        for i in range(len(coins)+1):
            for j in range(amount+1):
                if coins[i-1]<=j:
                    t[i][j]=min(t[i-1][j],t[i][j-coins[i-1]]+1)
                else:
                    t[i][j]=t[i-1][j]
        if t[-1][-1]==sys.maxsize-1:
            return -1
        else:
            return t[-1][-1]
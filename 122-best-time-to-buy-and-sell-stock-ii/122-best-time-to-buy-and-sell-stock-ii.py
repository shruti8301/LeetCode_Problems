class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=0
        for i in range(len(prices)-1,0,-1):
            if prices[i-1]<prices[i]:
                p+=prices[i]-prices[i-1]
        return p
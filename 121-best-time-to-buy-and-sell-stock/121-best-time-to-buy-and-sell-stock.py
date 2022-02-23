class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        c=prices[0]
        for i in range(1,len(prices)):
            if c<prices[i]:
                maxp=max(maxp,prices[i]-c)
            else:
                c=prices[i]
        return maxp
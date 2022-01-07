class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=0
        minimum=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<minimum:
                minimum=prices[i]
            else:
                p+=prices[i]-minimum
                minimum=prices[i]
        return p
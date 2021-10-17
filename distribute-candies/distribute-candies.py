class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n=len(candyType)//2
        candyType=set(candyType)
        if len(candyType)>=n:
            return n
        else:
            return len(candyType)
        
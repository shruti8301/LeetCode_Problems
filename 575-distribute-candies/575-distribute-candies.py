class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        a=len(candyType)//2
        candyType=set(candyType)
        if len(candyType)>=a:
            return a
        else:
            return len(candyType)
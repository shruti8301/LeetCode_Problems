class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        x=m
        y=n
        for i in ops:
            a=i[0]
            b=i[1]
            if a<x:
                x=a
            if b<y:
                y=b
        return x*y
                
            
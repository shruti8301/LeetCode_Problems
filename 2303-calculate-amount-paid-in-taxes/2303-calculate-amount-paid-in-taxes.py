class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        res = 0 
        prev = 0 
        for i, j in brackets:
            val = min(i, income)
            if val - prev > 0:
                res += j * (val - prev)/100
                prev = i
        return res 

                
            
class Solution:
    def convertToBase7(self, num: int) -> str:
        res = ""
        n = abs(num)    
        while n > 6:
            digit = n % 7
            res = res + str(digit)
            n = n//7
        y = (res + str(n))
        
        if num < 0:
            return "-"+y[::-1]
        else:
            return y[::-1]
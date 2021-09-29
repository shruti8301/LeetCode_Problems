class Solution:
    def addDigits(self, num: int) -> int:
        a=[]
        while num:
            s=(num%10)
            num=num//10
            a.append(s)
        s=sum(a)
        if(s>=0 and s<=9):
            return(s)
        else:
            return (self.addDigits(s))
            
        
        
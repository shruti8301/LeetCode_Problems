class Solution:
    def atoi(self,s):
        result=0
        for i in s:
            result=result*10+ord(i)-ord('0')
        return result
    def itoa(self,num):
        s = [0 if not num else '']
        while num:
            s.append(chr(48 + num % 10))
            num = num // 10
        a= "".join(reversed(s))
        return a
    
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0":
            return "0"
        #print(self.atoi(num1))
        return (self.itoa(self.atoi(num1)*self.atoi(num2)))
    
    
    
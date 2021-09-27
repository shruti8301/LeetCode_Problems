class Solution:
    def reverse(self, x):
        self.r=0
        no=abs(x)
        while(no):
            self.r=self.r*10+(no%10)
            no=no//10
        if (self.r > 2**31 -1) or (-self.r < -2**31):
            return 0
        if x >= 0:
            return self.r
        else:
            return -self.r
    
            
        
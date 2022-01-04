class Solution:
    def numDecodings(self, s: str) -> int:
        
        if len(s)==0 or s==None: 
            return 0
        return self.decode(s)
    
    @lru_cache(maxsize=None)
    
    def decode(self,s):
        
        if len(s)>0 and s[0]=='0': 
            return 0
        if s=='' or len(s)==1: 
            return 1
        if int(s[:2])<=26: 
            return self.decode(s[1:])+self.decode(s[2:])
        else: 
            return self.decode(s[1:])
class Solution:
    def validPalindrome(self, s: str) -> bool:
        n=len(s)
        def pal(s1):
            return s1==s1[::-1]
        
        l=0
        r=n-1
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                return pal(s[l:r]) or pal(s[l+1:r+1])
        return True
            
                
                
        
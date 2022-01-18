class Solution:
    def toGoatLatin(self, s: str) -> str:
        v=['a','A','E','e','I','i','O','o','U','u']
        s=s.split()
        for i in range(len(s)):
            if s[i][0] in v:
                s[i]+='ma'
            else:
                s[i]=s[i][1:]+s[i][0]+'ma'
            s[i]+='a'*(i+1)
        return ' '.join(s)
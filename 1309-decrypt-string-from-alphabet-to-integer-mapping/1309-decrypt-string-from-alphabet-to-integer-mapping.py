class Solution:
    def freqAlphabets(self, s: str) -> str:
        i=len(s)-1
        ans=''
        while i>=0:
            if s[i]=='#':
                ans+=chr(int(s[i-2]+s[i-1])+96)
                i-=3
            else:
                ans+=chr(int(s[i])+96)
                i-=1
        return ans[::-1]  
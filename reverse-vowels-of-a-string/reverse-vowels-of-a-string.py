class Solution:
    def reverseVowels(self, s: str) -> str:
        x=''
        a=['a','e','i','o','u','A','E','I','O','U']
        v=[i for i in s if i in a]
        for i in s:
            if i in a:
                x+=v[-1]
                v.pop()
            else:
                x+=i
        return x
        
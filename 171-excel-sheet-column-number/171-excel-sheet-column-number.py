class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        c=0
        d=0
        for i in columnTitle[::-1]:
            a=ord(i)-64
            a*=26**c
            d+=a
            c+=1
        return d
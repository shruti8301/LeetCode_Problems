class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s=s.upper()
        li=s.split("-")
        st = "".join(li)[::-1]
        arr = []
        for i in range(0,len(st),k):
            arr.append(st[i:i+k])
        return "-".join(arr)[::-1]
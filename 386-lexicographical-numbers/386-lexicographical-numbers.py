class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        arr=[]
        for i in range(1,n+1):
            arr.append(str(i))
        arr.sort()
        r=[int(j) for j in arr]
        return r
class Solution:
    def countBits(self, n: int) -> List[int]:
        arr=[]
        a=[]
        for i in range (n+1):
            arr.append(i)
        for i in range (len(arr)):
            arr[i]=bin(arr[i])[2:]
            a.append(arr[i].count('1'))
        return a
                
                
            
        
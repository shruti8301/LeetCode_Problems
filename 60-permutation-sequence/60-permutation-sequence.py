
class Solution:
    def permutation(self,n,k):
        arr=[]
        for i in range(1,n+1):
            arr.append(str(i))
        #print(arr)
        permutations = list(itertools.permutations(arr))
        #print(permutations)
        a=[''.join(i) for i in permutations]
        return(a[k-1])
        
    def getPermutation(self, n: int, k: int) -> str:
        return(self.permutation(n,k))
        
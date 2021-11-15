class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr=[]
        def backtrack(start,combinations):
            if len(combinations)==k:
                arr.append(combinations.copy())
            for i in range(start,n+1):
                combinations.append(i)
                backtrack(i+1,combinations)
                combinations.pop()
        backtrack(1,[])
        return arr
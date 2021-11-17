class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        arr=[]
        def decision(i,c,total):
            if total==target:
                arr.append(c.copy())
                return
            if i>=len(candidates) or total>target:
                return 
            for j in range(i,len(candidates)):
                if j>i and candidates[j] == candidates[j-1]:
                    continue
                c.append(candidates[j])
                decision(j+1,c,total+candidates[j])
                c.pop()
        decision(0,[],0)
        return arr
            
        
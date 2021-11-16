class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        arr=[]
        def decision(i,c,total):
            if total==target:
                arr.append(c.copy())
                return
            if i>=len(candidates) or total>target:
                return 
            c.append(candidates[i])
            decision(i,c,total+candidates[i])
            c.pop()
            decision(i+1,c,total)
        decision(0,[],0)
        return arr
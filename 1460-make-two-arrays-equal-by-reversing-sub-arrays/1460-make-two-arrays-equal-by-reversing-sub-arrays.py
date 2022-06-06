from collections import Counter
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target.sort()
        arr.sort()
        a=Counter(target)
        b=Counter(arr)
        if a==b:
            return True
       # print(a,b)
                
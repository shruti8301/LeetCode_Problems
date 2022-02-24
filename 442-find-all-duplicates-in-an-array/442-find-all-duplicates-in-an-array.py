from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        arr=[]
        a=Counter(nums)
        print(a)
        for i in a:
            if a[i]==2 or a[i]==3:
                arr.append(i)
        return arr
            
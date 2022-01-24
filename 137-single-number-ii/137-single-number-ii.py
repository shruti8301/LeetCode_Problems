
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = defaultdict(int)
        for num in nums:
            a[num]+=1
            if a[num] == 3:
                del a[num]
        
        return list(a.keys())[0]
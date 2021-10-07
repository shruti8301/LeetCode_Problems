class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        s=set(nums)
        arr=set()
        for i in range(1,n+1):
            arr.add(i)
        return list(arr.difference(s))
        
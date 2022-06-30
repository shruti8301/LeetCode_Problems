class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return 0
        nums.sort()
        print(nums)
        a=len(nums)-1
        mid=a//2
        suma=0
        print(nums[mid])
        for i in range(len(nums)):
            suma+=abs(nums[i]-nums[mid])
            print(suma)
        #print(sum(nums))
        return suma
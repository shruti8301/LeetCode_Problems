class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        s=set()
        nums.sort()
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                l=j+1
                r=n-1
                while l<r:
                    sumt=nums[i]+nums[j]+nums[l]+nums[r]
                    if sumt<target:
                        l+=1
                    elif sumt>target:
                        r-=1
                    else:
                        s.add((nums[i],nums[j],nums[l],nums[r]))
                        l+=1
                        r-=1
        return [list(i) for i in s]
        
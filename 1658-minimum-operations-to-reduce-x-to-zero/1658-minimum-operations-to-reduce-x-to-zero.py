class Solution:
       def minOperations(self, nums: List[int], x: int) -> int:
        maxl = -1  # length of substring with target 
        n = len(nums)
        if n == 0: return maxl
        target = sum(nums) -x 
        leftptr = 0
        rightptr = 0
        s = 0
        while leftptr <= n and rightptr <= n :
            if s < target:
                rightptr += 1
                if rightptr <= n: s += nums[rightptr-1]
            elif s > target:
                leftptr += 1
                if leftptr < n: s -= nums[leftptr-1]
            else:
                maxl = max(maxl,rightptr - leftptr)
                rightptr += 1
                if rightptr <= n: s += nums[rightptr-1]
            if rightptr == n and s < target:  # no need to continue
                break
        if maxl != -1:
            return n - maxl   
        else:
            return -1
                
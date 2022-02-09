class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
    
    
        if k > 0:
            ans = 0
            # we go over the numbers, and look 
            # for num + k in hash table i.e the number whose abs diff with num equals k
            for j in d.keys():
                if j + k in d:
                    ans += 1

            return ans
    
        if k == 0:
            ans = 0
        # we go over the freq cnt values for numbers, where freq > 1
        # cause abs(num - num) makes 0
            for i in d.values():
                if i > 1:
                    ans += 1

            return ans
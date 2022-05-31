class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        for i in range(len(nums)):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i) # from large to small
            if q[0] <= i-k: # check if the head of q is valid
                q.popleft() 
            if i+1 >= k: # when q is equal to k, add the first num
                res.append(nums[q[0]])
        return res
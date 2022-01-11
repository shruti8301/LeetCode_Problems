class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n=len(nums)
        
        if n==1:
            return nums[0]
        
        wo_first = [-1]*(n)
        w_first = [-1]*(n)
        
        wo_first[0]=0
        wo_first[1]=nums[1]
        
        w_first[0]=nums[0]
        w_first[1]=nums[0]

        for i in range(2,n):
                w_first[i] = max(w_first[i-1],nums[i]+w_first[i-2])
                wo_first[i] = max(wo_first[i-1],nums[i]+wo_first[i-2])
                
        return max(wo_first[-1],w_first[-2])
       
        
        
                
        
    
                
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        arraySum=sum(nums)
        print(arraySum//2)
        if arraySum%2!=0:
            return False
        else:
            return self.subsetsum(nums,arraySum//2)
        
    def subsetsum(self,nums,Sum):
        t=[[0 for x in range(Sum+1)] for x in range(len(nums)+1)]
       
        
        for i in range (len(nums)+1):
            for j in range(Sum+1):
                t[0][j]=False     
                t[i][0]=True
                        
                if nums[i-1]<=j:
                    t[i][j]=t[i-1][j-nums[i-1]] or t[i-1][j]
                else:
                    t[i][j]=t[i-1][j]
        return t[-1][-1]
        
        
        
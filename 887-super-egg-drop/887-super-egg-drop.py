class Solution:
    """
    Time Complexity: O(k*n* log(n))
    Space Complexity: k*n
    """
    def __init__(self):
        self.t = []
    
    def superEggDrop(self, k: int, n: int) -> int:
        self.t = [[-1 for _ in range(n+1)] for _ in range(k+1)]        
        return self.solve(k,n)
    
    def solve(self,k,n):
        # If we have only one egg, we have to check all the floors
        # If the no of floor is 1, then the move will be 1
        # If the no of floor is 0, then no movement is required and result is 0
        if k == 1 or n == 1 or n == 0:
            return n
        
        # Caching
        if self.t[k][n] != -1:
            return self.t[k][n]
        
        ans = float('inf')
        
        low = 0
        high = n
        
        while low <= high:
            mid = (low + high) // 2
            
            # When the Egg breaks
            left = self.solve(k-1,mid-1)
            
            # When Egg will not break
            right = self.solve(k, n-mid)
            
            # No of moves increase -> 1 + max moves between (left and light)
            temp = 1 + max(left,right)
            
            if left < right:
                low = mid+1
            else:
                high = mid-1
            
            # Find the minimum move
            ans = min(ans,temp)
            
            # Updating the matrix
            self.t[k][n] = ans
        return ans
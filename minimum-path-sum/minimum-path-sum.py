class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        length=0
        for i in range(row-1,-1,-1):
            for j in range(col-1,-1,-1):
                
                if i==row-1 and j!=col-1:
                    grid[i][j]+=grid[i][j+1]
                elif i!=row-1 and j==col-1:
                    grid[i][j]+=grid[i+1][j]
                    
                elif i!=row-1 and j!=col-1:
                    grid[i][j]+=min(grid[i][j+1],grid[i+1][j])
        return grid[0][0]
        
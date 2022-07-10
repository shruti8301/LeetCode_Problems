class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row=[]
        col=[]
        for i in range(len( matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    row.append(i)
                    col.append(j)
        for c in col:
            for i in range(len( matrix)):
                matrix[i][c]=0
        #print(matrix)
        for r in row:
            for j in range(len(matrix[0])):
                matrix[r][j]=0
        print(matrix)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board)     #row
        n=len(board[0])  #col
        visited=set()
        
        def findword(board,word,row,col,i=0):
            if i==len(word):
                return True
            if row>=len(board) or col>=len(board[0]) or row<0 or col<0 or word[i]!=board[row][col] or (row,col) in visited:
                return False
            visited.add((row,col)) 
            r=findword(board,word,row,col+1,i+1) or findword(board,word,row+1,col,i+1) or findword(board,word,row,col-1,i+1) or findword(board,word,row-1,col,i+1)
            visited.remove((row,col))
            return r    
        for i in range(m):
            for j in range(n):
                    if findword(board,word,i,j):
                        return True
        return False
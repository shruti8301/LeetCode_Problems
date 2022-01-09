class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r=[set() for _ in range(9)]
        c=[set() for _ in range(9)]
            
        box=[set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                v=board[i][j]
                
                if v == ".":
                    continue
                    
                if v in r[i]:
                    return False
                r[i].add(v)
                if v in c[j]:
                    return False
                c[j].add(v)
                box_id=(i//3)*3+j//3
                if v in box[box_id]:
                    return False
                box[box_id].add(v)
        return True
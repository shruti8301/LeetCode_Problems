class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x=0
        y=0
        moves=list(moves)
        for i in moves:
            if i=="U":
                y+=1
            if i=="D":
                y-=1
            if i=="L":
                x-=1
            if i=="R":
                x+=1
        if x==0 and y==0:
            return True
        
        
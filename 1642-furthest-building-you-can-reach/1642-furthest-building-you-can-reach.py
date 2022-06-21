class Solution:
    def furthestBuilding(self, h: List[int], bricks: int, ladders: int) -> int:
        climb=[]
        heapq.heapify(climb)
        for i in range(1,len(h)):
            if h[i]<h[i-1]:
                continue
            diff = h[i]-h[i-1]
            if ladders>0:
                ladders-=1
                heapq.heappush(climb,diff)
            else:
                heapq.heappush(climb,diff)
                bricks_used = heapq.heappop(climb)
                if bricks-bricks_used>=0:
                    bricks-=bricks_used
                else:
                    return i-1
        return len(h)-1
class Solution:
    def maxArea(self, h: int, w: int, hc: List[int], vc: List[int]) -> int:
        hc,vc = sorted(hc + [0,h]),sorted(vc + [0,w])
        return max([b-a for a,b in zip(hc,hc[1:])]) * max([b-a for a,b in zip(vc,vc[1:])]) % (10**9+7)
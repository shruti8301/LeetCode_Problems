class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        if not jewels or not stones:
            return 0
        a=0
        for i in jewels:
            if i in stones:
                a+=stones.count(i)
        return a
        
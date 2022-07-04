class Solution:
    def candy(self, ratings: List[int]) -> int:
        z = sorted([(i, r) for i, r in enumerate(ratings)], key=lambda x: (x[1], x[0]))
        d = [-1 for _ in range(len(ratings))]

        for i, v in z:
            c = 0
            # check left
            if i > 0 and d[i-1] != -1 and ratings[i-1] < v:
                c = d[i-1] + 1
            # check right
            if i < len(ratings) -1 and d[i+1] != -1 and ratings[i+1] < v:
                c = max(c, d[i+1]+1)

            if c == 0:
                c = 1

            d[i] = c

        return sum(d)
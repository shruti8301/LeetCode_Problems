class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        k = 2
        i = 0
        j = 0
        d = dict()
        max_size = 0
        while (j < len(fruits)):
            if fruits[j] in d: # If fruit in already in collected from trees we can collect more
                max_size = max(max_size, j-i+1)
                d[fruits[j]] += 1
                j += 1
            else: # If fruit is new
                if len(d) < k: # If we have basket to collect we can collect this new fruit
                    max_size = max(max_size, j-i+1)
                    d[fruits[j]] = 1
                    j += 1
                elif len(d) == k and i < len(fruits):
                # If we do not have more basket and this fruit is new we will drop out from left until we can collect this new fruit
                    if fruits[i] in d:
                        d[fruits[i]] -= 1
                    if fruits[i] in d and d[fruits[i]] == 0:
                        d.pop(fruits[i])
                    i += 1
        return max_size
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key=lambda x: x[::-1])
        print(words)
        ans = 0
        for i, j in pairwise(words):
            if not j.endswith(i):
                ans += len(i) + 1
        return ans + len(words[-1]) + 1
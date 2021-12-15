class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ret = []
        wl = len(words[0])
        wordsused = []
        
        for i in range (0, len(s) - len(words) * wl + 1):
            test = s[i:i+wl]
            if test in words:
                for j in range(0, len(words) * wl, wl):
                    curr = s[i+j:i+j+wl]
                    if curr in words:
                        words.remove(curr)
                        wordsused.append(curr);
                    else:
                        break
                if len(words) == 0:
                    ret.append(i)
                    words = wordsused
                    wordsused = []
                else:
                    for w in wordsused:
                        words.append(w)
                    wordsused = []
                    
        return ret
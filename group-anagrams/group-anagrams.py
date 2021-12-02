class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_of_anagrams = defaultdict(list)
        arr=[]
        for i in strs:
            sorted_characters = sorted(i)
            a = "".join(sorted_characters)
            group_of_anagrams[a].append(i)
            #print(group_of_anagrams)
        for j in group_of_anagrams:
            arr.append(group_of_anagrams[j])
        return arr
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = [restaurant for restaurant in list1 if restaurant in list2]
        index_sum = [(list1.index(i) + list2.index(i)) for i in common]
        
        return [common[i] for i in range(len(index_sum)) if index_sum[i]==min(index_sum)]
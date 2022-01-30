class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        number_lines = 1
        sums = 0
        for num in s:
            value = widths[ord(num)-97]
            if ((sums+value)>100):
                sums=value
                number_lines+=1
            else:
                sums+=value
        output = [number_lines,sums]
        return output
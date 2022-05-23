import datetime
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        str1=date1.split("-")
        str2=date2.split("-")
        d1=date(int(str1[0]),int(str1[1]),int(str1[2]))
        d2=date(int(str2[0]),int(str2[1]),int(str2[2]))
        diff=abs(d1-d2)
        return diff.days
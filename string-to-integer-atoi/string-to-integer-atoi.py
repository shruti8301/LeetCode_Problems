class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s)==0:
            return 0
        sign = "+"
        if (s[0]=="-" or s[0]=="+"):
            sign = s[0]
            s = s[1:]
            if (len(s)==0 or not s[0].isdigit()):
                return 0
        if (not s[0].isdigit()):
            return 0
        else:
            i = 0
            result = ""
            while (i<len(s) and s[i].isdigit()):
                result+=s[i]
                i+=1
            if (sign=="-"):
                result = int(result)*-1
                if result <= pow(-2,31):
                    return -2147483648
                else:
                    return result
            else:
                result = int(result)
                if result > pow(2,31) - 1:
                    return 2147483647
                else:
                    return result
        
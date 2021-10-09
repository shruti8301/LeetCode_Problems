class Solution:
    def lengthOfLongestSubstring(self, s):
        ans=''
        r=0
        for i in s:
            if i not in ans:
                ans+=i
            else:
                if len(ans)>r:
                    r=len(ans)
                ans=ans[1:]
                while i in ans:
                    ans=ans[1:]
                ans+=i
        if len(ans)>r:
            r=len(ans)
        return r
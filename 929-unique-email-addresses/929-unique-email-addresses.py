class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emailset = set()
        for i in emails:
            l,g = i.split("@")
            l = l.split('+')[0].replace('.', '')
            emailset.add(l.join(g))
        return len(emailset)
        
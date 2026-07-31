class Solution:
    def removeStars(self, s: str) -> str:
        a=[]
        for i in range(len(s)):
            if s[i]=='*' and len(a)!=0:
                a.pop()
            else:
                a.append(s[i])

        return "".join(a)
                
        
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        t=set('aeiou')
        sub=s[:k]
        m=0
        c=0
        for i in range(len(sub)):
            if sub[i] in t:
                c+=1
        m=max(m,c)
        for i in range(k,len(s)):
            if s[i] in t:
                c+=1
            if s[i-k] in t:
                c-=1
            m=max(m,c)
        return m

# sub=sub[1:]+s[i]    this is correct
# sub=sub+s[i]-s[i-k]  this is incorrect
        
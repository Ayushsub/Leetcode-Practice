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
        
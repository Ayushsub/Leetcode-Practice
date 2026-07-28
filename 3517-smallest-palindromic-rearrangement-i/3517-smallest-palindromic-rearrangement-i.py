class Solution:
    def smallestPalindrome(self, s: str) -> str:
        l=len(s)
        if l==1 or l==2 or l==3:
            return s
        t=list(s[:l//2])
        t.sort()
        t=''.join(t)
        if l%2==0:
            ans=t[:]+t[::-1]
        else:
            ans=t[:]+s[l//2]+t[::-1]
        return ans

        
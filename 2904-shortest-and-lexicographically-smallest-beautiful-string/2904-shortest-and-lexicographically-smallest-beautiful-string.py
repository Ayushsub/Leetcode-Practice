class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        p=[i for i,c in enumerate(s) if c=='1']
        if len(p)<k:return""
        ans=""
        m=float('inf')
        for i in range(len(p)-k+1):
            t=s[p[i]:p[i+k-1]+1]
            if len(t)<m or len(t)==m and t<ans:
                m=len(t)
                ans=t
        return ans
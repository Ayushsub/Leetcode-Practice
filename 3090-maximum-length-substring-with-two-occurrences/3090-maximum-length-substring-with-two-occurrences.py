class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        d={}
        left=0
        ans=0
        for right in range(len(s)):
            d[s[right]]=d.get(s[right],0)+1
            while d[s[right]]>2:
                d[s[left]]-=1
                left+=1
            ans=max(ans,right-left+1)
        return ans
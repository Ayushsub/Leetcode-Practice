from collections import Counter
from math import comb
class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq=Counter(s)
        half={}
        mid=""
        for ch in freq:
            half[ch]=freq[ch]//2
            if freq[ch]%2:
                mid=ch
        rem=sum(half.values())

        def countWays():
            left=rem
            ways=1
            for c in half.values():
                if c:
                    ways*=comb(left,c)
                    if ways>=k:
                        return k
                    left-=c
            return ways

        if countWays()<k:
            return ""

        ans=[]
        while rem:
            for ch in sorted(half):
                if half[ch]==0:
                    continue
                half[ch]-=1
                rem-=1
                ways=countWays()
                if ways>=k:
                    ans.append(ch)
                    break
                k-=ways
                half[ch]+=1
                rem+=1

        first="".join(ans)
        return first+mid+first[::-1]
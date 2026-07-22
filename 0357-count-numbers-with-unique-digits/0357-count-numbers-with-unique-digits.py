class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n==0:
            return 1
        ans=10
        cur=9
        avail=9
        while n>1 and avail>0:
            cur*=avail
            ans+=cur
            avail-=1
            n-=1
        return ans
        
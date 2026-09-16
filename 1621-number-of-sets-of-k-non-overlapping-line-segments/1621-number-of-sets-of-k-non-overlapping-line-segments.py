class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        m=10**9+7
        r=1
        for i in range(1,2*k+1):
            r=r*(n+k-i)*pow(i,m-2,m)%m
        return r
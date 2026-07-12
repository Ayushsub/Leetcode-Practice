class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        M_od=10**9+7
        r=k
        c=0
        cc=1
        for x in nums:
            if r<x:
                t=(x-r+k-1)//k
                c=(c+t*(2*cc+t-1)//2)%M_od
                cc+=t
                r+=t*k
            r=r-x
        return c
            
      
        